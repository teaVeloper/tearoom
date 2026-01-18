#!/usr/bin/env bash
# Simple volume controller with OSD via dunstify.
# Works for PulseAudio and PipeWire (through pactl).

STEP=5
SINK="@DEFAULT_SINK@"
RID=7779  # replace-id to update the same toast

get_vol() {
  pactl get-sink-volume "$SINK" | awk -F'/' 'NR==1{gsub(/%| /,"",$2); print $2}'
}

get_mute() {
  pactl get-sink-mute "$SINK" | awk '{print $2}'
}

show_osd() {
  vol="$(get_vol)"
  mute="$(get_mute)"
  if [ "$mute" = "yes" ]; then
    icon="󰝟"  # muted
    text="Muted"
  else
    # pick a rough icon by volume
    if   [ "$vol" -lt 34 ]; then icon="󰕿"
    elif [ "$vol" -lt 67 ]; then icon="󰖀"
    else                         icon="󰕾"
    fi
    text="${vol}%"
  fi

  dunstify -a "volume" -r "$RID" "$icon  $text"
}

case "$1" in
  up)   pactl set-sink-volume "$SINK" +${STEP}% ;;
  down) pactl set-sink-volume "$SINK" -${STEP}% ;;
  mute) pactl set-sink-mute   "$SINK" toggle   ;;
  *)    echo "Usage: $0 {up|down|mute}"; exit 1 ;;
esac

show_osd

