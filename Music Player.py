import flet as ft
import flet_audio as fta

def main(page: ft.Page):

    songs = [
        "Eyedress & Dent May - Something About You.mp3",
        "KSI - Thick Of It (feat. Trippie Redd) [Official Music Video].mp3",
        "Tame Impala - Borderline (Official Audio).mp3",
        "TV Girl - Lovers Rock (Lyrics).mp3",
        "Mac DeMarco  Freaking Out The Neighborhood.mp3"
    ]

    estado = {"index1": 0, "is_paused": False}
    audio_player = fta.Audio(src=songs[estado["index1"]])
    page.overlay.append(audio_player)

    def play_audio(e):
        if estado["is_paused"] == False:
            audio_player.resume()
        else:
            audio_player.play()
        estado["is_paused"] = True

    def pause_audio(e):
        audio_player.pause()
        estado["is_paused"] = True

    def next_song(e):
        if songs[estado["index1"]]:
            estado["index1"] += 1
            if estado["index1"] > 4:
                estado["index1"]=0
            audio_player.src = songs[estado["index1"]]
            page.update()
            audio_player.play()
            estado["is_paused"] = False

    def prev_song(e):
        if estado["index1"] > 0:
            estado["index1"] -= 1
            if estado["index1"] < 0:
                estado["index1"] = 4
            audio_player.src = songs[estado["index1"]]
            page.update()
            audio_player.play()
            estado["is_paused"] = False

    prev_button = ft.ElevatedButton(text="Previous Song", on_click=prev_song)
    play_button = ft.ElevatedButton(text="Play", on_click=play_audio)
    pause_button = ft.ElevatedButton(text="Pause", on_click=pause_audio)
    next_button = ft.ElevatedButton(text="Next Song", on_click=next_song)


    page.add(prev_button, play_button, pause_button, next_button)


ft.app(target=main)

