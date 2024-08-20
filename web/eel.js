let isPlaying = false;

function jsPlayPause() {
    eel.PlayPause();
    isPlaying = !isPlaying;
    document.getElementById("playpause").textContent = isPlaying ? "Pause" : "Play";
}

function jsPlayNext() {
    eel.nextTrack();
}

function jsPlayPrevious() {
    eel.previousTrack();
}

eel.expose(rename);
function rename(title) {
    title = title.replace('.mp3', '');
    document.getElementById("songTitle").textContent = title;
}
