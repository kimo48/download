<?php

#$red = #"\033[1;31m";
#$green = #"\033[1;32m";
#$blue = #"\033[1;34m";
#$pink = #"\033[1;35m";
#$bluesky = "#\033[1;36m";
system('clear');

$banner2 = "\033[1;31mUpdating default packages \n\n";
echo $banner2;
system('apt update && apt upgrade -y');

echo "\033[1;32mRequesting acces to storage\n";
sleep(2);
echo "\033[1;33mAllow Storage Permission!\n";
sleep(2);
system('termux-setup-storage -y');
sleep(5);
system('clear');

echo "\033[1;34mInstalling vim\n";
system('pkg install vim -y');

echo "\033[1;35mInstalling python\n";
system('pkg install python -y');

echo "\033[1;36mInstalling php\n";
system('pkg install php -y');

echo "\033[1;34mupgrade pip\n";
system('pip install --upgrade pip');

echo "\033[1;36mInstalling ffmpeg\n";
system('pkg install ffmpeg -y');

echo "\033[1;34mInstalling requests\n";
system('pip install requests');

echo "\033[1;34mInstalling bs4\n";
system('pip install bs4');

echo "\033[1;34mInstalling re\n";
system('pip install regex');

echo "\033[1;34mInstalling flask\n";
system('pip install flask');

echo "\033[1;34mInstalling cloudscraper\n";
system('pip install cloudscraper');

echo "\033[1;34mInstalling tqdm\n";
system('pip install tqdm');

echo "\033[1;34mInstalling rich\n";
system('pip install rich');

echo "\033[1;34mInstalling youtube-dl\n";
system('pip install youtube-dl');

echo "\033[1;34mInstalling youtube_dl\n";
system('pip install youtube_dl');

echo "\033[1;34mInstalling yt-dlp\n";
system('pip install yt-dlp');

echo "\033[1;32mMaking the Youtube Directory to download the Vidoes\n";
system('mkdir ~/storage/shared/f_Youtube');

echo "\033[1;32mMaking the Tiktok Directory to download the Vidoes\n";
system('mkdir ~/storage/shared/f_Tiktok');

echo "\033[1;32mMaking the Facebook Directory to download the Vidoes\n";
system('mkdir ~/storage/shared/f_Facebook');

echo "\033[1;32mMaking the insta Directory to download the Vidoes\n";
system('mkdir ~/storage/shared/f_instagram');

echo "\033[1;32mCreating youtube-dl folder for config\n";
system('mkdir -p ~/.config/youtube-dl');

echo "Creating bin folder\n";
system('mkdir ~/bin');

echo "Creating Termux-URL-Opener FILE.\n";
system('mv termux-url-opener ~/bin/');
system('clear');

echo "\n";
echo "\033[1;32mProcess Complete!\n";
echo "\033[1;37m[\033[1;32m+\033[1;37m]\033[1;37m ==========[\033[1;33mkarim\033[1;37m]==========\033[1;37m [\033[1;32m+\033[1;37m]\n\n";
