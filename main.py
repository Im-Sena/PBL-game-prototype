import random
import pygame
from pygame.locals import *
import sys

from text import Text

wX, wY = 1000, 600  # 画面サイズ
JPFONT = "NotoSansJP-VariableFont_wght.ttf"  # 日本語フォントのパス
word = "word"  # ワードウルフのキーワード
# プレイヤー情報クラス
class Player:
    def __init__(self, name="", is_wolf=False):
        self.name = name  # プレイヤー名
        self.is_wolf = is_wolf  # 人狼ならTrue、村人ならFalse

    def set_wolf(self, is_wolf: bool):
        """人狼かどうかを設定するメソッド"""
        self.is_wolf = is_wolf

    def is_werewolf(self):
        """人狼かどうかを返すメソッド"""
        return self.is_wolf

# ゲーム設定クラス
class GameSettings:
    def __init__(self, player_count=4, wolf_count=1, think_time=1, discuss_time=3):
        self.player_count = player_count      # プレイヤー人数
        self.wolf_count = wolf_count          # ワードウルフ人数
        self.think_time = think_time          # 考える時間（分）
        self.discuss_time = discuss_time      # 議論時間（分）
        
# タイトル画面用のクラス
class TitleScene:
    def __init__(self):
        self.fontTitle = pygame.font.Font(JPFONT, 80)  # タイトル用フォント
        self.button = pygame.Rect(wX/2-100, wY/2+50, 200, 100)  # スタートボタン

    def update(self, screen, events):
        screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし
        # タイトルテキスト描画
        text = self.fontTitle.render("TITLE", True, (255, 255, 255))
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

        # Y座標の起点
        base_y = wY//4 - 100
        gap = 100

        # 各種ボタン
        self.button_plus = pygame.Rect(wX/2+160, base_y, 40, 40)
        self.button_minus = pygame.Rect(wX/2-200, base_y, 40, 40)

        self.button_wolf_plus = pygame.Rect(wX/2+160, base_y+gap, 40, 40)
        self.button_wolf_minus = pygame.Rect(wX/2-200, base_y+gap, 40, 40)

        self.button_think_plus = pygame.Rect(wX/2+160, base_y+gap*2, 40, 40)
        self.button_think_minus = pygame.Rect(wX/2-200, base_y+gap*2, 40, 40)

        self.button_discuss_plus = pygame.Rect(wX/2+160, base_y+gap*3, 40, 40)
        self.button_discuss_minus = pygame.Rect(wX/2-200, base_y+gap*3, 40, 40)

        self.button = pygame.Rect(wX/2-100, wY/2+150, 200, 100)
        self.pushFlag = False  # 連打防止用

        self.thinkTime = 1
        self.discussTime = 3

    def update(self, screen, events):
        screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし
        base_y = wY//4 - 100
        gap = 100

        # プレイヤー人数表示
        text = self.fontTitle.render(f"player count : {self.playerCount}", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, base_y+20))
        screen.blit(text, text_Title)
        pygame.draw.rect(screen, (0, 200, 0), self.button_plus)
        plus_text = self.fontTitle.render("+", True, (255,255,255))
        plus_rect = plus_text.get_rect(center=self.button_plus.center)
        screen.blit(plus_text, plus_rect)
        pygame.draw.rect(screen, (200, 0, 0), self.button_minus)
        minus_text = self.fontTitle.render("-", True, (255,255,255))
        minus_rect = minus_text.get_rect(center=self.button_minus.center)
        screen.blit(minus_text, minus_rect)

        # ワードウルフ人数表示
        text = self.fontTitle.render(f"wolf count : {self.wolfCount}", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, base_y+gap+20))
        screen.blit(text, text_Title)
        pygame.draw.rect(screen, (0, 200, 0), self.button_wolf_plus)
        plus_text = self.fontTitle.render("+", True, (255,255,255))
        plus_rect = plus_text.get_rect(center=self.button_wolf_plus.center)
        screen.blit(plus_text, plus_rect)
        pygame.draw.rect(screen, (200, 0, 0), self.button_wolf_minus)
        minus_text = self.fontTitle.render("-", True, (255,255,255))
        minus_rect = minus_text.get_rect(center=self.button_wolf_minus.center)
        screen.blit(minus_text, minus_rect)

        # 考える時間表示
        text = self.fontTitle.render(f"think time : {self.thinkTime} min", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, base_y+gap*2+20))
        screen.blit(text, text_Title)
        pygame.draw.rect(screen, (0, 200, 0), self.button_think_plus)
        plus_text = self.fontTitle.render("+", True, (255,255,255))
        plus_rect = plus_text.get_rect(center=self.button_think_plus.center)
        screen.blit(plus_text, plus_rect)
        pygame.draw.rect(screen, (200, 0, 0), self.button_think_minus)
        minus_text = self.fontTitle.render("-", True, (255,255,255))
        minus_rect = minus_text.get_rect(center=self.button_think_minus.center)
        screen.blit(minus_text, minus_rect)

        # 議論時間表示
        text = self.fontTitle.render(f"discuss time : {self.discussTime} min", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, base_y+gap*3+20))
        screen.blit(text, text_Title)
        pygame.draw.rect(screen, (0, 200, 0), self.button_discuss_plus)
        plus_text = self.fontTitle.render("+", True, (255,255,255))
        plus_rect = plus_text.get_rect(center=self.button_discuss_plus.center)
        screen.blit(plus_text, plus_rect)
        pygame.draw.rect(screen, (200, 0, 0), self.button_discuss_minus)
        minus_text = self.fontTitle.render("-", True, (255,255,255))
        minus_rect = minus_text.get_rect(center=self.button_discuss_minus.center)
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
            # 考える時間増減
            if self.button_think_plus.collidepoint(mx, my):
                if self.thinkTime < 10:
                    self.thinkTime += 1
            if self.button_think_minus.collidepoint(mx, my):
                if self.thinkTime > 1:
                    self.thinkTime -= 1
            # 議論時間増減
            if self.button_discuss_plus.collidepoint(mx, my):
                if self.discussTime < 30:
                    self.discussTime += 1
            if self.button_discuss_minus.collidepoint(mx, my):
                if self.discussTime > 1:
                    self.discussTime -= 1
            # OKボタン
            if self.button.collidepoint(mx, my):
                print(f"設定完了: プレイヤー人数={self.playerCount}, ワードウルフ人数={self.wolfCount}, 考える時間={self.thinkTime}分, 議論時間={self.discussTime}分")
                self.pushFlag = True
                pygame.display.flip()
                return True
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
        self.editing_text = ""
        
        pygame.key.start_text_input()

    def update(self, screen, events):
        prompt = self.font.render(f"Player {self.current_index+1} の名前を入力してください", True, (255,255,255))
        screen.fill((0, 0, 0))
        screen.blit(prompt, (50, 50))

        event_trigger = {
            pygame.K_BACKSPACE: self.text.delete_left_of_cursor,
            pygame.K_DELETE: self.text.delete_right_of_cursor,
            pygame.K_LEFT: self.text.move_cursor_left,
            pygame.K_RIGHT: self.text.move_cursor_right,
            pygame.K_RETURN: self.text.enter,
        }

        input_text = str(self.text)

        for event in events:
            if event.type == pygame.KEYDOWN and not self.text.is_editing:
                if event.key in event_trigger.keys():
                    input_text = event_trigger[event.key]()
                if event.unicode in ("\r", "") and event.key == pygame.K_RETURN:
                    entered_name = input_text.replace("|", "")
                    self.players[self.current_index].name = entered_name
                    self.current_index += 1
                    self.text = Text()
                    self.editing_text = ""
                    print(f"Player {self.current_index} の名前: {entered_name}")
                    if self.current_index >= len(self.players):
                        pygame.key.stop_text_input()
                        pygame.display.flip()
                        return True
                    pygame.key.start_text_input()  # 念のため再度有効化
                    break
            elif event.type == pygame.TEXTEDITING:
                # 変換中のテキストだけ保存（Textクラスには反映しない）
                self.editing_text = event.text
            elif event.type == pygame.TEXTINPUT:
                # 確定した文字だけTextクラスに反映
                input_text = self.text.input(event.text)
                self.editing_text = ""

        # --- ここで確定前のテキスト＋暫定テキストを合成して描画 ---
        display_text = str(self.text)
        if self.editing_text:
            cursor_pos = display_text.find("|")
            if cursor_pos != -1:
                display_text = display_text[:cursor_pos] + self.editing_text + display_text[cursor_pos:]
            else:
                display_text += self.editing_text

        input_surface = self.font.render(display_text, True, (255,255,255))
        screen.blit(input_surface, (50, 120))
        pygame.display.flip()
        return False

# ゲーム画面
class GameScene:
    def __init__(self, players, gameSettings):
        self.players = players
        self.font = pygame.font.Font(JPFONT, 40)
        self.startButton = pygame.Rect(wX/2+100, wY/2+150, 200, 100)
        self.backButton = pygame.Rect(wX/2-300, wY/2+150, 200, 100)
        self.checkButton = pygame.Rect(wX/2+100, wY/2+150, 200, 100)
        self.pushFlag = False  # 連打防止用
        self.current_player_index = 0
        self.state = "confirm"
        self.gameSettings = gameSettings
        self.started = False  # ← 追加

    def check_start_conditions(self, screen, events):
        screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし

        text = self.font.render(f"参加者", True, (255, 255, 255))
        text_Title = text.get_rect(center=(wX/2, wY/4))
        screen.blit(text, text_Title)
        # プレイヤーの名前を表示
        for i, player in enumerate(self.players):
            player_text = self.font.render(f"{i+1}人目: {player.name}", True, (255, 255, 255))
            player_rect = player_text.get_rect(center=(wX/2, wY/4 + (i+2) * 50))
            screen.blit(player_text, player_rect)
        # ゲーム開始ボタン
        pygame.draw.rect(screen, (255, 0, 0), self.startButton)
        start_text = self.font.render("START", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=self.startButton.center)
        screen.blit(start_text, start_rect)
        # 戻るボタン
        pygame.draw.rect(screen, (0, 0, 255), self.backButton)
        back_text = self.font.render("BACK", True, (255, 255, 255))
        back_rect = back_text.get_rect(center=self.backButton.center)
        screen.blit(back_text, back_rect)
        # マウスクリック処理
        mdown = pygame.mouse.get_pressed() 
        mx, my = pygame.mouse.get_pos()
        if mdown[0] and not self.pushFlag:
            if self.startButton.collidepoint(mx, my):
                print("ゲーム開始")
                self.pushFlag = True
                pygame.display.flip()
                # 人狼を設定画面の人数分ランダムで選ぶ
                wolf_indices = random.sample(range(len(self.players)), self.gameSettings.wolf_count)
                for i, player in enumerate(self.players):
                    player.set_wolf(i in wolf_indices)
                    if player.is_werewolf():
                        print(f"{player.name} は人狼です")
                    else:
                        print(f"{player.name} は村人です")
                return True
            if self.backButton.collidepoint(mx, my):
                print("設定画面に戻る")
                self.pushFlag = True
                pygame.display.flip()
                return False
        #ここでpushFlagをリセット
        if not mdown[0]:
            self.pushFlag = False

        pygame.display.flip()
        return False

    def update(self, screen, events):
        # ...（今まで通りのupdate処理）...
        screen.fill((0, 0, 0))
        player = self.players[self.current_player_index]

        if self.state == "confirm":
            # 名前確認
            text = self.font.render(f"あなたは{player.name}ですか？", True, (255, 255, 255))
            text_rect = text.get_rect(center=(wX/2, wY/4))
            screen.blit(text, text_rect)
            pygame.draw.rect(screen, (0, 255, 0), self.checkButton)
            check_text = self.font.render("はい", True, (255, 255, 255))
            check_rect = check_text.get_rect(center=self.checkButton.center)
            screen.blit(check_text, check_rect)

            mdown = pygame.mouse.get_pressed()
            mx, my = pygame.mouse.get_pos()
            if mdown[0] and not self.pushFlag:
                if self.checkButton.collidepoint(mx, my):
                    self.state = "show_word"
                    self.pushFlag = True
            if not mdown[0]:
                self.pushFlag = False

        elif self.state == "show_word":
            # お題・役職表示
            if player.is_werewolf():
                role_text = f"{player.name} は人狼でお題は「{word}」です"
            else:
                role_text = f"{player.name} は村人でお題は「{word}」です"
            text = self.font.render(role_text, True, (255, 255, 255))
            text_rect = text.get_rect(center=(wX/2, wY/2))
            screen.blit(text, text_rect)
            # 「次へ」ボタン（checkButtonを再利用）
            pygame.draw.rect(screen, (0, 200, 200), self.checkButton)
            next_text = self.font.render("次へ", True, (255, 255, 255))
            next_rect = next_text.get_rect(center=self.checkButton.center)
            screen.blit(next_text, next_rect)

            mdown = pygame.mouse.get_pressed()
            mx, my = pygame.mouse.get_pos()
            if mdown[0] and not self.pushFlag:
                if self.checkButton.collidepoint(mx, my):
                    self.current_player_index += 1
                    if self.current_player_index >= len(self.players):
                        print("全員確認終了")
                        return True
                    else:
                        self.state = "confirm"
                    self.pushFlag = True
            if not mdown[0]:
                self.pushFlag = False

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
                think_time = scene.thinkTime
                discuss_time = scene.discussTime
                players = [Player() for _ in range(player_count)]
                gameSettings.player_count = player_count
                gameSettings.wolf_count = wolf_count
                gameSettings.think_time = think_time
                gameSettings.discuss_time = discuss_time
                scene = PlayerNameInput(players)

        # プレイヤー名入力画面
        elif isinstance(scene, PlayerNameInput):
            if scene.update(screen, events):
                scene = GameScene(players, gameSettings)

        # ゲームシーン
        elif isinstance(scene, GameScene):
            if not scene.started:
                if scene.check_start_conditions(screen, events):
                    scene.started = True  # 一度だけTrueにする
            else:
                if scene.update(screen, events):
                    # 全員確認終了などでTrueが返ったら次のシーンへ
                    pass

if __name__ == "__main__":
    main()