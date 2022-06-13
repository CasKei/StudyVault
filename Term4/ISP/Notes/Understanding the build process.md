---
aliases: gradle
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

The Android application package (APK) is the package file format for distributing and installing Android mobile apps. The build process involves tools and processes that automatically convert each project into an APK.

Android Studio uses Gradle as the foundation of the build system, with more Android-specific capabilities provided by the Android Plugin for Gradle. This build system runs as an integrated tool from the Android Studio menu.

## build.gradle files
When you create a project, Android Studio automatically generates the necessary build files in the `Gradle Scripts` folder in the **Project > Android** pane. Android Studio build files are named `build.gradle`

### build.gradle (Project: _apptitle_)

This file is the top-level build file for the entire project, located in the root project folder, which defines build configurations that apply to all modules in your project. This file, generated by Android Studio, should not be edited to include app dependencies.

If a dependency is something other than a local library or file tree, Gradle looks for the files in whichever online repositories are specified in the repositories block of this file. By default, new Android Studio projects declare JCenter and Google (which includes the [Google Maven repository](https://maven.google.com/)) as the repository locations:
```groovy
allprojects {
    repositories {
        google()
        jcenter()
    }
}
```

### build.gradle (Module: app)
Android Studio creates separate `build.gradle (Module: app)` files for each module. You can edit the build settings to provide custom packaging options for each module, such as additional build types and product flavors, and to override settings in the manifest or top-level build.gradle file. This file is most often the file to edit when changing app-level configurations, such as declaring dependencies in the `dependencies` section. The following shows the contents of a project's `build.gradle (Module: app)` file:
```groovy
apply plugin: 'com.android.application'

android {
    compileSdkVersion 26
    defaultConfig {
        applicationId "com.example.android.helloworld"
        minSdkVersion 15
        targetSdkVersion 26
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner 
                         "android.support.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 
                                                     'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'com.android.support:appcompat-v7:26.1.0'
    implementation 'com.android.support.constraint:constraint-layout:1.0.2'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'com.android.support.test:runner:1.0.1'
    androidTestImplementation 
                    'com.android.support.test.espresso:espresso-core:3.0.1'
}
```
The `build.gradle` files use Gradle syntax. Gradle is a Domain Specific Language (DSL) for describing and manipulating the build logic using [Groovy](http://groovy-lang.org/), which is a dynamic language for the Java Virtual Machine (JVM). You don't need to learn Groovy to make changes, because the Android Plugin for Gradle introduces most of the DSL elements you need.

**Tip**: To learn more about the Android plugin DSL, read the [DSL reference documentation](http://google.github.io/android-gradle-dsl/current/index.html).

#### Plugin and Android blocks
In the `build.gradle (Module: app)` file above, the first statement applies the Android-specific Gradle plug-in build tasks:
```
apply plugin: 'com.android.application'

android {
   compileSdkVersion 26
   // ... Rest of android block.
}
```
The `android { }` block specifies the target SDK version for compiling the app code ( `compileSdkVersion 26`) and several blocks of information.

#### The defaultConfig block
Core settings and entries for the app are specified in the `defaultConfig { }` block within the `android { } block:`
```groovy
defaultConfig {
    applicationId "com.example.android.helloworld"
    minSdkVersion 15
    targetSdkVersion 26
    versionCode 1
    versionName "1.0"
    testInstrumentationRunner 
                "android.support.test.runner.AndroidJUnitRunner"
}
```
The `minSdkVersion` and `targetSdkVersion` settings override any `AndroidManifest.xml` settings for the minimum SDK version and the target SDK version. See "Declaring the Android version" previously in this chapter for background information on these settings.

The `testInstrumentationRunner` statement adds the instrumentation support for testing the UI using Espresso and UIAutomator. These tools are described in a separate lesson.

#### Build types
Build types for the app are specified in a `buildTypes { }` block, which controls how the app is built and packaged.
```groovy
buildTypes {
    release {
        minifyEnabled false
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 
                                                       'proguard-rules.pro'
    }
}
```
The build type specified is `release` for the app's release. Another common build type is `debug`. Configuring build types is described in a separate lesson.

#### Dependencies
Dependencies for the app are defined in the `dependencies { }` block, which is the part of the `build.gradle` file that is most likely to change as you start developing code that depends on other libraries. The block is part of the standard Gradle API and belongs _outside_ the `android { }` block.
```groovy
dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'com.android.support:appcompat-v7:26.1.0'
    implementation 'com.android.support.constraint:constraint-layout:1.0.2'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'com.android.support.test:runner:1.0.1'
    androidTestImplementation 
                    'com.android.support.test.espresso:espresso-core:3.0.1'
}
```
In the snippet above, the statement `implementation fileTree(dir: 'libs', include: ['*.jar'])` adds a dependency of all ".jar" files inside the `libs` folder.

### Syncing your project
When you make changes to the build configuration files in a project, Android Studio requires that you _sync_ the project files. During the sync, Android Studio imports the build configuration changes and runs checks to make sure the configuration won't create build errors.

To sync the project files, click **Sync Now** in the notification bar that appears when making a change, or click the **Sync Project with Gradle Files** button ![ Sync Project with Gradle Files ](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-1-c-your-first-android-app/ic_gradle_sync.png " Sync Project with Gradle Files ") in the menu bar

If Android Studio notices any errors with the configuration — for example, if the source code uses API features that are only available in an API level higher than the `compileSdkVersion`—the **Messages** window appears to describe the issue.