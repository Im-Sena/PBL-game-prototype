import pygame
from pygame.locals import *
import sys

from text import Text

wX, wY = 1000, 600  # 画面サイズ
JPFONT = "NotoSansJP-VariableFont_wght.ttf"  # 日本語フォントのパス

# プレイヤー情報クラス
class Player:
    def __init__(self, name=""):
        self.name = name  # プレイヤー名

# ゲーム設定クラス
class GameSettings:
    def __init__(self, player_count=4, wolf_count=1, discuss_time=180):
        self.player_count = player_count      # プレイヤー人数
        self.wolf_count = wolf_count          # ワードウルフ人数
        self.discuss_time = discuss_time      # 議論時間（秒）

# タイトル画面用のクラス
class TitleScene:
    def __init__(self):
        self.fontTitle = pygame.font.Font(JPFONT, 80)  # タイトル用フォント
        self.button = pygame.Rect(wX/2-100, wY/2+50, 200, 100)  # スタートボタン

    def update(self, screen, events):
        screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし
        # タイトルテキスト描画
        text = self.fontTitle.render("Hello, World", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, wY/4))
        screen.blit(text, text_Title)
        # スタートボタン描画
        pygame.draw.rect(screen, (255, 0, 0), self.button)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.button.collidepoint(mx, my):
                    return True  # ボタンが押されたら次のシーンへ
        pygame.display.flip()
        return False

# 設定画面クラス
class Settings:
    def __init__(self):
        self.fontTitle = pygame.font.Font(JPFONT, 40)
        self.playerCount = 2
        self.wolfCount = 1
        self.time = 3
        # 各種ボタン
        self.button_plus = pygame.Rect(wX/2+120, wY/4-20, 40, 40)
        self.button_minus = pygame.Rect(wX/2-160, wY/4-20, 40, 40)
        self.button_wolf_plus = pygame.Rect(wX/2+120, wY/4+80, 40, 40)
        self.button_wolf_minus = pygame.Rect(wX/2-160, wY/4+80, 40, 40)
        self.button_time_plus = pygame.Rect(wX/2+120, wY/4+180, 40, 40)
        self.button_time_minus = pygame.Rect(wX/2-160, wY/4+180, 40, 40)
        self.button = pygame.Rect(wX/2-100, wY/2+150, 200, 100)
        self.pushFlag = False  # 連打防止用

    def update(self, screen, events):
        screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし
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
        if mdown[0] and not self.pushFlag:
            # プレイヤー人数増減
            if self.button_plus.collidepoint(mx, my):
                if self.playerCount < 8:
                    self.playerCount += 1
            if self.button_minus.collidepoint(mx, my):
                if self.playerCount > 2:
                    self.playerCount -= 1
            # ワードウルフ人数増減
            if self.button_wolf_plus.collidepoint(mx, my):
                if self.wolfCount < self.playerCount-1:
                    self.wolfCount += 1
            if self.button_wolf_minus.collidepoint(mx, my):
                if self.wolfCount > 1:
                    self.wolfCount -= 1
            # 議論時間増減
            if self.button_time_plus.collidepoint(mx, my):
                if self.time < 30:
                    self.time += 1
            if self.button_time_minus.collidepoint(mx, my):
                if self.time > 1:
                    self.time -= 1
            # 決定ボタン
            if self.button.collidepoint(mx, my):
                print(f"設定完了: プレイヤー人数={self.playerCount}, ワードウルフ人数={self.wolfCount}, 議論時間={self.time}分")
                self.pushFlag = True
                pygame.display.flip()
                return True  # 次のシーンへ
            self.pushFlag = True
        if not mdown[0]:
            self.pushFlag = False

        pygame.display.flip()
        return False

# プレイヤー名入力画面
class PlayerNameInput:
    def __init__(self, players):
        self.players = players
        self.text = Text()
        self.current_index = 0
        self.font = pygame.font.Font(JPFONT, 40)
        self.editing_text = ""  # IME変換中のテキスト

    def update(self, screen, events):
        # 入力プロンプト
        prompt = self.font.render(f"Player {self.current_index+1} の名前を入力してください", True, (255,255,255))
        screen.fill((0, 0, 0))
        screen.blit(prompt, (50, 50))

        # キーイベントとTextクラスの対応
        event_trigger = {
            pygame.K_BACKSPACE: self.text.delete_left_of_cursor,
            pygame.K_DELETE: self.text.delete_right_of_cursor,
            pygame.K_LEFT: self.text.move_cursor_left,
            pygame.K_RIGHT: self.text.move_cursor_right,
            pygame.K_RETURN: self.text.enter,
        }

        input_text = str(self.text)

        for event in events:
            # テキスト入力処理
            if event.type == pygame.KEYDOWN and not self.text.is_editing:
                if event.key in event_trigger.keys():
                    input_text = event_trigger[event.key]()
                # Enterで確定
                if event.unicode in ("\r", "") and event.key == pygame.K_RETURN:
                    entered_name = input_text.replace("|", "")
                    self.players[self.current_index].name = entered_name
                    self.current_index += 1
                    self.text = Text()
                    self.editing_text = ""
                    print(f"Player {self.current_index} の名前: {entered_name}")
                    if self.current_index >= len(self.players):
                        pygame.display.flip()
                        return True  # 全員分入力したら次のシーンへ
                    break
            elif event.type == pygame.TEXTEDITING:
                # IME変換中のテキストを保存
                self.editing_text = event.text
                input_text = self.text.edit(event.text, event.start)
            elif event.type == pygame.TEXTINPUT:
                input_text = self.text.input(event.text)
                self.editing_text = ""  # 確定したら消す

        # --- ここで確定前のテキスト＋暫定テキストを合成して描画 ---
        display_text = str(self.text)
        if self.editing_text:
            # カーソル位置に暫定テキストを挿入
            cursor_pos = display_text.find("|")
            if cursor_pos != -1:
                display_text = display_text[:cursor_pos] + self.editing_text + display_text[cursor_pos:]
            else:
                display_text += self.editing_text

        # 入力中のテキストを表示
        input_surface = self.font.render(display_text, True, (255,255,255))
        screen.blit(input_surface, (50, 120))
        pygame.display.flip()
        return False

# ゲーム画面
class GameScene:
    def __init__(self, players):
        self.players = players

    def update(self, screen, events):
        screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし
        font = pygame.font.Font(JPFONT, 40)
        # 1人目の名前を表示
        text = font.render(f"1人目の名前: {self.players[0].name}", True, (255,255,255))
        screen.blit(text, (50, 50))
        pygame.display.flip()
        return False

# メインループ
def main():
    pygame.init()
    screen = pygame.display.set_mode((wX, wY))
    pygame.display.set_caption("pbl-game-protype")
    scene = TitleScene()
    running = True
    gameSettings = GameSettings()
    players = [Player() for _ in range(4)]
    pygame.key.start_text_input()  # IME入力を有効化

    while running:
        events = pygame.event.get()  # イベントはここで1回だけ取得
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # タイトル画面
        if isinstance(scene, TitleScene):
            if scene.update(screen, events):
                scene = Settings()

        # 設定画面
        elif isinstance(scene, Settings):
            if scene.update(screen, events):
                player_count = scene.playerCount
                wolf_count = scene.wolfCount
                discuss_time = scene.time
                players = [Player() for _ in range(player_count)]
                gameSettings.player_count = player_count
                gameSettings.wolf_count = wolf_count
                gameSettings.discuss_time = discuss_time
                scene = PlayerNameInput(players)

        # プレイヤー名入力画面
        elif isinstance(scene, PlayerNameInput):
            if scene.update(screen, events):
                scene = GameScene(players)

        # ゲームシーン
        elif isinstance(scene, GameScene):
            scene.update(screen, events)

if __name__ == "__main__":
    main()