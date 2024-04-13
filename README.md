# starting
npx expo start
# Building 
npm install -g eas-cli
eas build --platform android
github link : https://github.com/google/bundletool/...
java -jar bundletool.jar build-apks --bundle=filename.aab --output=newfilename.apks --mode=universal

keytool -genkeypair -alias androiddebugkey -keypass android -keystore debug.keystore -storepass android -dname "CN=Android Debug,O=Android,C=US" -validity 9999
java -jar bundletool-all-1.15.6.jar build-apks --bundle=app.aab --output=output.apks --mode=universal --ks=debug.keystore --ks-key-alias=androiddebugkey
