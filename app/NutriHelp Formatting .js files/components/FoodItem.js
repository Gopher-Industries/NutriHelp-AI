import * as React from "react";
import {
  View,
  StyleSheet,
  Text,
  Pressable,
  Image,
  ImageBackground,
} from "react-native";

const FoodItem = () => {
  return (
    <View style={styles.bananaView}>
      <View style={styles.bananaBorderView} />
      <Text style={styles.banana1}>
        <Text style={styles.banana}>Banana</Text>
      </Text>
      <Pressable style={styles.bananaAddCircleButton}>
        <Image
          style={styles.iconssettingsFilled24px}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.bananaAddButtonIcon}
        resizeMode="cover"
        source={require("../assets/bananaaddbutton.png")}
      />
      <Text style={styles.kJPerServing}>{`328 KJ - per serving `}</Text>
      <ImageBackground
        style={styles.bananaImageIcon}
        resizeMode="cover"
        source={require("../assets/bananaimage.png")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  bananaBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 64,
  },
  banana: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  banana1: {
    position: "absolute",
    top: 6,
    left: 83,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  iconssettingsFilled24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  bananaAddCircleButton: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 276,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  bananaAddButtonIcon: {
    position: "absolute",
    height: "21.88%",
    width: "4.27%",
    top: "39.06%",
    right: "7.62%",
    bottom: "39.06%",
    left: "88.11%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJPerServing: {
    position: "absolute",
    top: 30,
    left: 83,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 171,
    height: 26,
  },
  bananaImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 70,
    height: 62,
  },
  bananaView: {
    position: "absolute",
    top: 352,
    left: 16,
    width: 328,
    height: 64,
  },
});

export default FoodItem;
