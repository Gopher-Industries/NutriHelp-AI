import * as React from "react";
import { Image, StyleSheet, View, Text, Pressable } from "react-native";
import { useNavigation } from "@react-navigation/native";

const WelcomeScreen1 = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.welcomeScreen1}>
      <Image
        style={styles.vector715493Icon}
        resizeMode="cover"
        source={require("../assets/vector-7154935.png")}
      />
      <Image
        style={styles.vector715493Icon1}
        resizeMode="cover"
        source={require("../assets/vector-7154932.png")}
      />
      <Image
        style={styles.vectorFFFBFEIcon}
        resizeMode="cover"
        source={require("../assets/vector-fffbfe1.png")}
      />
      <View style={styles.rectangleView} />
      <Image
        style={styles.vectorE7DFF0Icon}
        resizeMode="cover"
        source={require("../assets/vector-e7dff04.png")}
      />
      <Image
        style={styles.imageIcon}
        resizeMode="cover"
        source={require("../assets/image5.png")}
      />
      <Text style={styles.hi}>Hi!</Text>
      <Image
        style={styles.scrollIcon}
        resizeMode="cover"
        source={require("../assets/scroll5.png")}
      />
      <Text style={styles.tellUsYourNutrientRelated}>
        Tell us your nutrient-related diseases, deficiencies and dietary
        requirements
      </Text>
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("WelcomeScreen2")}
      >
        <Text style={styles.labelText}>Get Started</Text>
      </Pressable>
    </View>
  );
};

const styles = StyleSheet.create({
  vector715493Icon: {
    position: "absolute",
    top: 0,
    left: 0,
    width: 360,
    height: 310,
  },
  vector715493Icon1: {
    position: "absolute",
    top: 24,
    left: 0,
    width: 360,
    height: 510,
  },
  vectorFFFBFEIcon: {
    position: "absolute",
    top: 14,
    left: 0,
    width: 360,
    height: 575,
  },
  rectangleView: {
    position: "absolute",
    top: 384,
    left: -26,
    backgroundColor: "#fffbfe",
    width: 412,
    height: 280,
  },
  vectorE7DFF0Icon: {
    position: "absolute",
    top: 92,
    left: 0,
    width: 360,
    height: 388,
  },
  imageIcon: {
    position: "absolute",
    height: "48.06%",
    width: "113.89%",
    top: "20%",
    right: "-13.89%",
    bottom: "31.94%",
    left: "0%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  hi: {
    position: "absolute",
    top: 112,
    left: 159,
    fontSize: 32,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 42,
    height: 36,
  },
  scrollIcon: {
    position: "absolute",
    top: 438,
    left: 150,
    width: 61,
    height: 8,
  },
  tellUsYourNutrientRelated: {
    position: "absolute",
    top: 496,
    left: 22,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    width: 329,
    height: 41,
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
  button: {
    position: "absolute",
    top: 562,
    left: 22,
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
  welcomeScreen1: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default WelcomeScreen1;
