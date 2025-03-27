import * as React from "react";
import {
  View,
  StyleSheet,
  Text,
  ImageBackground,
  Pressable,
  Image,
} from "react-native";

const MealItemWithAddButton = () => {
  return (
    <View style={styles.oatmealView}>
      <View style={styles.oatmealBorderView} />
      <Text style={styles.oatmeal}>Oatmeal</Text>
      <Text style={styles.kJ}>{`536 KJ `}</Text>
      <ImageBackground
        style={styles.oatmealImageIcon}
        resizeMode="cover"
        source={require("../assets/4848007023532374350-2.png")}
      />
      <Pressable style={styles.oatmealAddButtonCircle}>
        <Image
          style={styles.iconssettingsFilled24px}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.oatmealAddButtonIcon}
        resizeMode="cover"
        source={require("../assets/bananaaddbutton.png")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  oatmealBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 169,
  },
  oatmeal: {
    position: "absolute",
    top: 116,
    left: 6,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 20,
  },
  kJ: {
    position: "absolute",
    top: 139,
    left: 6,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  oatmealImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  oatmealAddButtonCircle: {
    position: "absolute",
    marginTop: -75.5,
    top: "50%",
    left: 107,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  oatmealAddButtonIcon: {
    position: "absolute",
    height: "8.28%",
    width: "8.97%",
    top: "13.02%",
    right: "14.1%",
    bottom: "78.7%",
    left: "76.92%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  oatmealView: {
    position: "absolute",
    top: 288,
    left: 188,
    width: 156,
    height: 169,
  },
});

export default MealItemWithAddButton;
