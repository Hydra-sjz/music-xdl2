if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hydra-sjz/music-xdl.git /music-xdl
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /music-xdl
fi
cd /Midukki-RoBoT
pip3 install -U -r requirements.txt
echo "Starting music-xdl-RoBot...."
python3 -m bot
