import pygame
from pygame.locals import *
import sys

wX, wY = 1000, 600  # 画面サイズ

# タイトル画面用のクラス
class TitleScene:
    def __init__(self):
        #self.screen = screen  # 描画先
        self.fontTitle = pygame.font.Font(None, 80)  # タイトル用フォント
        # ボタンの位置とサイズ
        self.button = pygame.Rect(wX/2-100, wY/2+50, 200, 100)
        self.pushFlag = False  # クリック状態を管理

    def update(self,screen):
        # マウスの状態を取得
        mdown = pygame.mouse.get_pressed()  # クリック状態
        (mx, my) = pygame.mouse.get_pos()   # マウスの位置

        # 画面を黒色で塗りつぶし
        screen.fill((0, 0, 0))

        # タイトルテキストを描画
        text = self.fontTitle.render("Hello, World", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, wY/4))
        screen.blit(text, text_Title)

        # ボタンを描画
        pygame.draw.rect(screen, (255, 0, 0), self.button)

        # ボタンのクリックを1回だけ認識する処理
        if mdown[0]:  # 左クリックが押されている
            if self.button.collidepoint(mx, my) and not self.pushFlag:
                print("クリックされました")
                self.pushFlag = True  # クリックされたことを記録
        else:
            self.pushFlag = False  # クリック解除

        # 画面を更新
        pygame.display.flip()



    

def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((wX, wY))  # 画面を作成
    pygame.display.set_caption("pbl-game-protype")  # タイトル設定
    scene = TitleScene()  # タイトルシーンを作成
    running = True  # ループ制御用フラグ

    while running:
        # イベント処理
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        # シーンの更新・描画
        scene.update(screen)

if __name__ == "__main__":
    main()