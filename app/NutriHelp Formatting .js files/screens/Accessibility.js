import * as React from "react";
import { useState } from "react";
import {
  Text,
  StyleSheet,
  StatusBar,
  View,
  Pressable,
  Image,
  Switch,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const Accessibility = () => {
  const [switchValue, setSwitchValue] = useState(true);
  const [switch1Value, setSwitch1Value] = useState(false);
  const navigation = useNavigation();

  return (
    <View style={styles.accessibility}>
      <Text style={styles.termsOfService}>Terms of service</Text>
      <Text style={styles.theFollowingOptionsMayMake}>
        <Text style={styles.theFollowingOptions}>
          The following options may make using the app easier for you
        </Text>
      </Text>
      <Text style={styles.textSize}>Text Size</Text>
      <Text style={styles.colourBlind}>Colour Blind</Text>
      <Text style={styles.voiceOver}>Voice Over</Text>
      <StatusBar barStyle="default" translucent={true} />
      <View style={styles.topAppBar}>
        <Pressable
          style={styles.leadingIcon}
          onPress={() => navigation.goBack()}
        >
          <Image
            style={styles.icon}
            resizeMode="cover"
            source={require("../assets/leadingicon13.png")}
          />
        </Pressable>
        <Text style={styles.headline}>{`Accessibility  `}</Text>
        <View style={styles.trailingIcon}>
          <Image
            style={styles.trailingIcon3}
            resizeMode="cover"
            source={require("../assets/trailing-icon-310.png")}
          />
          <Image
            style={[styles.trailingIcon2, styles.ml24]}
            resizeMode="cover"
            source={require("../assets/trailing-icon-210.png")}
          />
          <Image
            style={[styles.trailingIcon1, styles.ml24]}
            resizeMode="cover"
            source={require("../assets/trailing-icon-110.png")}
          />
        </View>
      </View>
      <Switch
        style={styles.switch}
        value={switchValue}
        onValueChange={setSwitchValue}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.switch1}
        value={switch1Value}
        onValueChange={setSwitch1Value}
        thumbColor="#79747e"
        trackColor={{ false: "#939393", true: "#e7e0ec" }}
      />
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("CreateAccount1")}
      >
        <Text style={styles.labelText}>Continue</Text>
      </Pressable>
      <Pressable style={styles.inputChip}>
        <Text style={styles.labelText1}>Large</Text>
      </Pressable>
      <Pressable style={styles.filterChip}>
        <Image
          style={styles.icon1}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText2, styles.ml8]}>Normal</Text>
      </Pressable>
      <View style={styles.lineView} />
    </View>
  );
};

const styles = StyleSheet.create({
  ml24: {
    marginLeft: 24,
  },
  ml8: {
    marginLeft: 8,
  },
  termsOfService: {
    position: "absolute",
    top: 668,
    left: 73,
    fontSize: 12,
    letterSpacing: -0.1,
    lineHeight: 18,
    fontFamily: "Inter",
    color: "#000",
    textAlign: "center",
    width: 194,
    height: 35,
  },
  theFollowingOptions: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  theFollowingOptionsMayMake: {
    position: "absolute",
    top: 179,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 329,
    height: 49,
  },
  textSize: {
    position: "absolute",
    top: 264,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 85,
    height: 24,
  },
  colourBlind: {
    position: "absolute",
    top: 404,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 99,
    height: 24,
  },
  voiceOver: {
    position: "absolute",
    top: 456,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 85,
    height: 32,
  },
  icon: {
    width: "100%",
    height: "100%",
  },
  leadingIcon: {
    position: "absolute",
    left: 16,
    top: 20,
    width: 24,
    height: 24,
  },
  headline: {
    position: "absolute",
    bottom: 20,
    left: 16,
    fontSize: 24,
    lineHeight: 32,
    fontFamily: "Open Sans",
    color: "#1c1b1f",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 328,
  },
  trailingIcon3: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  trailingIcon2: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  trailingIcon1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  trailingIcon: {
    position: "absolute",
    top: 20,
    right: 16,
    overflow: "hidden",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "flex-start",
    display: "none",
  },
  topAppBar: {
    position: "absolute",
    top: 56,
    bottom: 472,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  switch: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "62.5%",
    right: "4.17%",
    bottom: "32.5%",
    left: "81.39%",
  },
  switch1: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "71.25%",
    right: "4.44%",
    bottom: "23.75%",
    left: "81.11%",
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
    top: 528,
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
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  inputChip: {
    position: "absolute",
    top: 304,
    left: 188,
    borderRadius: 8,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    flexDirection: "row",
    paddingHorizontal: 12,
    paddingVertical: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  icon1: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  labelText2: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  filterChip: {
    position: "absolute",
    top: 304,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    flexDirection: "row",
    paddingLeft: 8,
    paddingTop: 6,
    paddingRight: 16,
    paddingBottom: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  lineView: {
    position: "absolute",
    top: 368,
    left: 16,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  accessibility: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default Accessibility;
