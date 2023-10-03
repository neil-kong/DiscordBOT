import time, discord, datetime, requests, pytesseract
# 導入discord.ext模組中的tasks工具
from discord.ext import tasks, commands
from PIL import Image

class TaskTimes(commands.Cog):
    # 設定每小時執行一次函式
    every_hour_time = [
        datetime.time(hour = i, minute = 2, tzinfo = datetime.timezone(datetime.timedelta(hours = 8)))
        for i in range(24)
    ]

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.every_hour.start()

    # 每小時發送報時訊息
    @tasks.loop(time = every_hour_time)
    async def every_hour(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(1157954102937010279)

        url = 'https://thegodofpumpkin.com/terrorzones/terrorzone.png'
        path = './d2r/terrorzone.png'
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            with open(path,'wb') as file_path:
                for chunck in res:
                    file_path.write(chunck)
        else:
            print("Error!! HTTP Request failed")

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img = Image.open(path)
        onlineTZ = pytesseract.image_to_string(img, lang='eng')

        TZ = {
            # Act 1.
            'Blood Moor / Blood Moor' : '鮮血荒地 / 邪惡洞窟',
            'Cold Plains / Cave Level 1 / Cave Level 2' : '冰冷之原 / 洞穴',
            'Burial Grounds / Crypt / Mausoleum' : '埋骨之地 / 墓地 / 大陵寢',
            'Stony Field' : '亂石曠野',
            'Tristram' : '崔斯特姆',
            'Dark Wood / Underground Passage Level 1 / Underground Passage Level 2' : '黑暗森林 / 地底通道',
            'Black Marsh / Hole Level 1 / Hole Level 2' : '黑色荒地 / 洞窟',
            'Forgotten Tower / Tower Cellar Level 1 / Tower Cellar Level 2 / Tower Cellar Level 3 / Tower Cellar Level 4 / Tower Cellar Level 5' : '遺忘之塔',
            'Barracks / Jail 1 / Jail 2 / Jail 3' : '兵營 / 監牢',
            'Pit Level 1 / Pit Level 2' : '地穴',
            'Cathedral / Catacombs Level 1 / Catacombs Level 2 / Catacombs Level 3 / Catacombs Level 4' : '大教堂 / 地下墓穴',
            'Moo Moo Farm' : '哞哞農場',

            # Act 2.
            'Sewers Level 1 / Sewers Level 2 / Sewers Level 3' : '魯高因下水道',
            'Rocky Waste / Stony Tomb Level 1 / Stony Tomb Level 2' : '碎石荒地 / 古老石墓',
            'Dry Hills / Halls of the Dead Level 1 / Halls of the Dead Level 2 / Halls of the Dead Level 3' : '乾土高地 / 死亡神殿',
            'Far Oasis' : '遙遠的綠洲',
            'Lost City / Valley of Snakes / Claw Viper Temple Level 1 / Claw Viper Temple Level 2' : '失落古城 / 群蛇峽谷 / 利爪蛇魔神殿',
            'Ancient Tunnels' : '古代通道',
            'Arcane Sanctuary' : '祕法聖殿',
            'Tal Rasha\'s Tomb' : '塔拉夏古墓',
            
            # Act 3.
            'Spider Forest / Spider Cavern' : '蜘蛛森林 / 蜘蛛洞窟',
            'Great Marsh' : '大沼澤',
            'Flayer Jungle / Flayer Dungeon Level 1 / Flayer Dungeon Level 2 / Flayer Dungeon Level 3' : '剝皮叢林 / 剝皮地牢',
            'Kurast Bazaar / Ruined Temple / Disused Fane' : '庫拉斯特市集 / 荒廢神殿 / 廢棄寺院',
            'Travincal' : '崔凡克',
            'Durance of Hate Level 1 / Durance of Hate Level 2 / Durance of Hate Level 3' : '憎恨囚牢',

            # Act 4.
            'Outer Steppes / Plains of Despair' : '外圍荒原 / 絕望平原',
            'City of the Damned / River of Flame' : '罪罰之城 / 火焰之河',
            'Chaos Sanctum' : '混沌魔殿',

            # Act 5.
            'The Bloody Foothills / Frigid Highlands / Abaddon' : '血腥丘陵 / 冰凍高地 / 亞巴頓',
            'Arreat Plateau / Hell2 (Pit of Acheron)' : '亞瑞特高原 / 冥河地穴',
            'Crystalized Cavern Level 1(CrystallinePassage) / Cellar of Pity (Frozen River)' : '水晶通道 / 冰凍之河',
            'Crystalized Cavern Level 2(Glacial Trail) / Echo Chamber (Drifter Cavern)' : '冰河小徑 / 漂泊者洞窟',
            'Nihlathaks Temple / Halls of Anguish / Halls of Pain / Halls of Vaught' : '尼拉塞克的神殿 / 悲痛之廳 / 痛苦之廳 / 瓦特之廳',
            'Glacial Caves Level 1(Ancient\'s Way) / Glacial Caves Level 2 (Icy Cellar)' : '先祖之路 / 冰窖',
            'The Worldstone Keep Level 1 / The Worldstone Keep Level 2 / The Worldstone Keep Level 3 / Throne of Destruction / The Worldstone Chamber' : '世界之石要塞 / 毀滅王座 / 世界之石大殿',
        }

        tzsp = onlineTZ.split("\n")
        tzsp2 = tzsp[1].split(":: ")
        
        try:
            nextTZ = TZ[tzsp2[1]]
        except:
            nextTZ = tzsp2[1]
        
        print(nextTZ)

        embed = discord.Embed(
            title =  'D2R next TerrorZone' + '\n' + nextTZ,
            url='https://thegodofpumpkin.com/terrorzones/terrorzone.png',
            color = discord.Color.random()
        )
        
        embed.set_image(url = 'https://thegodofpumpkin.com/terrorzones/terrorzone.png')
        await channel.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(TaskTimes(bot))
