import pygame
from pygame.locals import *
import sys

wX, wY = 1000, 600  # 画面サイズ

class Player:
    def __init__(self, name=""):
        self.name = name  # プレイヤー名

class GameSettings:
    def __init__(self, player_count=4, wolf_count=1, discuss_time=180):
        self.player_count = player_count      # プレイヤー人数
        self.wolf_count = wolf_count          # ワードウルフ人数
        self.discuss_time = discuss_time      # 議論時間（秒）



# タイトル画面用のクラス
class TitleScene:
    def __init__(self):
        #self.screen = screen  # 描画先
        self.fontTitle = pygame.font.Font(None, 80)  # タイトル用フォント
        # ボタンの位置とサイズ
        self.button = pygame.Rect(wX/2-100, wY/2+50, 200, 100)

    def update(self,screen):

        # 画面を黒色で塗りつぶし
        screen.fill((0, 0, 0))

        # タイトルテキストを描画
        text = self.fontTitle.render("Hello, World", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, wY/4))
        screen.blit(text, text_Title)

        # ボタンを描画
        pygame.draw.rect(screen, (255, 0, 0), self.button)

        # ボタンのクリックを1回だけ認識する処理
        if buttonClick(self.button):
            return True
        # 画面を更新
        pygame.display.flip()
        return False

#ボタンのクリック検知
def buttonClick(button):
    pushFlag = False  # クリック状態を管理

        # マウスの状態を取得
    mdown = pygame.mouse.get_pressed()  # クリック状態
    (mx, my) = pygame.mouse.get_pos()   # マウスの位置

    # ボタンのクリックを1回だけ認識する処理
    if mdown[0]:  # 左クリックが押されている
        if button.collidepoint(mx, my) and not pushFlag:
            print("クリックされました")
            pushFlag = True  # クリックされたことを記録
            return True
    else:
        pushFlag = False  # クリック解除




class Settings:
    def __init__(self):
        self.fontTitle = pygame.font.Font(None, 40)
        self.playerCount = 2
        self.wolfCount = 1
        self.time = 3
        # プレイヤー人数の増減ボタン
        self.button_plus = pygame.Rect(wX/2+120, wY/4-20, 40, 40)
        self.button_minus = pygame.Rect(wX/2-160, wY/4-20, 40, 40)
        # ワードウルフ人数の増減ボタン
        self.button_wolf_plus = pygame.Rect(wX/2+120, wY/4+80, 40, 40)
        self.button_wolf_minus = pygame.Rect(wX/2-160, wY/4+80, 40, 40)
        # 議論時間の増減ボタン
        self.button_time_plus = pygame.Rect(wX/2+120, wY/4+180, 40, 40)
        self.button_time_minus = pygame.Rect(wX/2-160, wY/4+180, 40, 40)
        # 決定ボタン
        self.button = pygame.Rect(wX/2-100, wY/2+150, 200, 100)

    def update(self, screen):
        screen.fill((0, 0, 0))

        # プレイヤー人数表示
        text = self.fontTitle.render(f"player count : {self.playerCount}", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, wY/4))
        screen.blit(text, text_Title)
        # +ボタン
        pygame.draw.rect(screen, (0, 200, 0), self.button_plus)
        plus_text = self.fontTitle.render("+", True, (255,255,255))
        plus_rect = plus_text.get_rect(center=self.button_plus.center)
        screen.blit(plus_text, plus_rect)
        # -ボタン
        pygame.draw.rect(screen, (200, 0, 0), self.button_minus)
        minus_text = self.fontTitle.render("-", True, (255,255,255))
        minus_rect = minus_text.get_rect(center=self.button_minus.center)
        screen.blit(minus_text, minus_rect)

        # ワードウルフ人数表示
        text = self.fontTitle.render(f"wolf count : {self.wolfCount}", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, wY/4+100))
        screen.blit(text, text_Title)
        # +ボタン
        pygame.draw.rect(screen, (0, 200, 0), self.button_wolf_plus)
        plus_text = self.fontTitle.render("+", True, (255,255,255))
        plus_rect = plus_text.get_rect(center=self.button_wolf_plus.center)
        screen.blit(plus_text, plus_rect)
        # -ボタン
        pygame.draw.rect(screen, (200, 0, 0), self.button_wolf_minus)
        minus_text = self.fontTitle.render("-", True, (255,255,255))
        minus_rect = minus_text.get_rect(center=self.button_wolf_minus.center)
        screen.blit(minus_text, minus_rect)

        # 議論時間表示
        text = self.fontTitle.render(f"time : {self.time} min", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, wY/4+200))
        screen.blit(text, text_Title)
        # +ボタン
        pygame.draw.rect(screen, (0, 200, 0), self.button_time_plus)
        plus_text = self.fontTitle.render("+", True, (255,255,255))
        plus_rect = plus_text.get_rect(center=self.button_time_plus.center)
        screen.blit(plus_text, plus_rect)
        # -ボタン
        pygame.draw.rect(screen, (200, 0, 0), self.button_time_minus)
        minus_text = self.fontTitle.render("-", True, (255,255,255))
        minus_rect = minus_text.get_rect(center=self.button_time_minus.center)
        screen.blit(minus_text, minus_rect)

        # 決定ボタン
        pygame.draw.rect(screen, (255, 0, 0), self.button)
        ok_text = self.fontTitle.render("OK", True, (255,255,255))
        ok_rect = ok_text.get_rect(center=self.button.center)
        screen.blit(ok_text, ok_rect)

        # マウスクリック処理
        mdown = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if mdown[0]:
            # プレイヤー人数
            if self.button_plus.collidepoint(mx, my):
                if self.playerCount < 8:
                    self.playerCount += 1
                pygame.time.wait(200)
            if self.button_minus.collidepoint(mx, my):
                if self.playerCount > 2:
                    self.playerCount -= 1
                pygame.time.wait(200)
            # ワードウルフ人数
            if self.button_wolf_plus.collidepoint(mx, my):
                if self.wolfCount < self.playerCount-1:
                    self.wolfCount += 1
                pygame.time.wait(200)
            if self.button_wolf_minus.collidepoint(mx, my):
                if self.wolfCount > 1:
                    self.wolfCount -= 1
                pygame.time.wait(200)
            # 議論時間
            if self.button_time_plus.collidepoint(mx, my):
                if self.time < 30:
                    self.time += 1
                pygame.time.wait(200)
            if self.button_time_minus.collidepoint(mx, my):
                if self.time > 1:
                    self.time -= 1
                pygame.time.wait(200)
            # 決定ボタン
            if self.button.collidepoint(mx, my):
                print(f"設定完了: プレイヤー人数={self.playerCount}, ワードウルフ人数={self.wolfCount}, 議論時間={self.time}分")
                return True

        pygame.display.flip()
        return False
    

#プレイヤーネーム入力画面

class GameScene:
    def __init__(self, players):
        self.players = players  # 4人分のプレイヤー情報
    
    def update(self,screen):
        # 例：1人目の名前を使う
        print(self.players[0].name)

    

def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((wX, wY))  # 画面を作成
    pygame.display.set_caption("pbl-game-protype")  # タイトル設定
    scene = TitleScene()  # タイトルシーンを作成
    running = True  # ループ制御用フラグ
    gameSettings = GameSettings()
    # 4人分のPlayerインスタンスを作る
    players = [Player() for _ in range(4)]




    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # タイトル画面のボタンが押されたらTrueを返すようにする
        if isinstance(scene, TitleScene):
            if scene.update(screen):  # ボタンが押されたら
                scene = Settings()  # ゲームシーンに切り替え
        else:
            scene.update(screen)


if __name__ == "__main__":

    main()