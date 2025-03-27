import * as React from "react";
import { Image, StyleSheet, View, Text, Pressable } from "react-native";
import { useNavigation } from "@react-navigation/native";

const SplashScreen = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.splashScreen}>
      <Image
        style={styles.vector715493Icon}
        resizeMode="cover"
        source={require("../assets/vector-7154937.png")}
      />
      <Image
        style={styles.vector715493Icon1}
        resizeMode="cover"
        source={require("../assets/vector-7154938.png")}
      />
      <Image
        style={styles.vectorFFFBFEIcon}
        resizeMode="cover"
        source={require("../assets/vector-fffbfe4.png")}
      />
      <Image
        style={styles.vectorE7DFF0Icon}
        resizeMode="cover"
        source={require("../assets/vector-e7dff07.png")}
      />
      <View style={styles.backgroundFFFBFE} />
      <Text style={styles.nutriHelp}>NutriHelp</Text>
      <Image
        style={styles.gopherLogoIcon}
        resizeMode="cover"
        source={require("../assets/GopherLogo.png")}
      />
      <Text style={styles.termsOfService}>Terms of Service</Text>
      <Pressable
        style={styles.getStartedButton}
        onPress={() => navigation.navigate("WelcomeScreen1")}
      >
        <Text style={styles.labelText}>Get Started</Text>
      </Pressable>
      <Pressable
        style={styles.haveAnAccountButton}
        onPress={() => navigation.navigate("Login")}
      >
        <Text style={styles.labelText1}>I already have an account</Text>
      </Pressable>
      <Text style={styles.nutriHelpSupportsYouInMana}>
        <Text style={styles.nutriHelpSupportsYou}>
          NutriHelp supports you in managing your general wellbeing,
          nutrient-related diseases and deficiencies through personalised
          nutrition advice
        </Text>
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  vector715493Icon: {
    position: "absolute",
    top: 0,
    left: 0,
    width: 360,
    height: 318,
  },
  vector715493Icon1: {
    position: "absolute",
    top: 30,
    left: 0,
    width: 360,
    height: 510,
  },
  vectorFFFBFEIcon: {
    position: "absolute",
    top: 22,
    left: 0,
    width: 360,
    height: 575,
  },
  vectorE7DFF0Icon: {
    position: "absolute",
    top: 99,
    left: 0,
    width: 360,
    height: 540,
  },
  backgroundFFFBFE: {
    position: "absolute",
    top: 304,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
    height: 344,
  },
  nutriHelp: {
    position: "absolute",
    top: 128,
    left: 104,
    fontSize: 32,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
  },
  gopherLogoIcon: {
    position: "absolute",
    height: "14.47%",
    width: "25.56%",
    top: "29.22%",
    right: "37.22%",
    bottom: "56.31%",
    left: "37.22%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  termsOfService: {
    position: "absolute",
    top: 571,
    left: 119,
    fontSize: 12,
    textDecoration: "underline",
    letterSpacing: -0.1,
    lineHeight: 18,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    width: 112,
    height: 21,
  },
  labelText: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "700",
    fontFamily: "Open Sans",
    color: "#fff",
    textAlign: "center",
  },
  getStartedButton: {
    position: "absolute",
    top: 464,
    left: 16,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    width: 328,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  labelText1: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "700",
    fontFamily: "Open Sans",
    color: "#8273a9",
    textAlign: "center",
  },
  haveAnAccountButton: {
    position: "absolute",
    top: 520,
    left: 16,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  nutriHelpSupportsYou: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  nutriHelpSupportsYouInMana: {
    position: "absolute",
    top: 336,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    width: 328,
    height: 87,
  },
  splashScreen: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default SplashScreen;
