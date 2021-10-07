curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip

curl https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip > chromedriver.zip

mkdir -p bin/
unzip -o headless-chromium.zip -d bin/
unzip -o chromedriver.zip -d bin/
rm -r *.zip

zip -r chrome-binary.zip bin
rm -r bin