import * as React from "react";
import {
  StatusBar,
  StyleSheet,
  View,
  Pressable,
  Image,
  Text,
  TextInput,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const DislikesAddedByYou = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.dislikesAddedByYou}>
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
        <Text style={styles.headline}>Dislikes</Text>
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
      <Text style={styles.mostCommon}>Most Common</Text>
      <TextInput
        style={styles.dislikesSearchTextInput}
        placeholder="Search Dislikes"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
      <View style={styles.raisinsButton}>
        <Text style={styles.labelText}>Raisins</Text>
      </View>
      <View style={styles.anchoviesButton}>
        <Text style={styles.labelText1}>Anchovies</Text>
      </View>
      <View style={styles.noneButton}>
        <Text style={styles.labelText2}>None</Text>
      </View>
      <View style={styles.tofuButton}>
        <Text style={styles.labelText3}>Tofu</Text>
      </View>
      <View style={styles.gingerButton}>
        <Image
          style={styles.icon1}
          resizeMode="cover"
          source={require("../assets/icon12.png")}
        />
        <Text style={[styles.labelText4, styles.ml8]}>Ginger</Text>
      </View>
      <View style={styles.mushroomsButton}>
        <Image
          style={styles.icon2}
          resizeMode="cover"
          source={require("../assets/icon12.png")}
        />
        <Text style={[styles.labelText5, styles.ml8]}>Mushrooms</Text>
      </View>
      <Pressable
        style={styles.continueButton}
        onPress={() => navigation.navigate("HealthConditions2")}
      >
        <Text style={styles.labelText6}>Continue</Text>
      </Pressable>
      <Text style={styles.addedByYou}>Added by you</Text>
      <Pressable style={styles.avocadoAddedButton}>
        <Image
          style={styles.icon3}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText7, styles.ml8]}>Avocado</Text>
      </Pressable>
      <Pressable style={styles.coconutAddedbutton}>
        <Image
          style={styles.icon4}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText8, styles.ml8]}>Coconut</Text>
      </Pressable>
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
    color: "#000",
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
  mostCommon: {
    position: "absolute",
    top: 344,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 192,
    height: 32,
  },
  dislikesSearchTextInput: {
    position: "absolute",
    top: 176,
    left: 16,
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#1c1b1f",
    borderWidth: 1,
    width: 328,
    height: 56,
  },
  labelText: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  raisinsButton: {
    position: "absolute",
    top: 432,
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
  anchoviesButton: {
    position: "absolute",
    top: 480,
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
  labelText2: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  noneButton: {
    position: "absolute",
    top: 384,
    left: 16,
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
  labelText3: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  tofuButton: {
    position: "absolute",
    top: 480,
    left: 16,
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
  labelText4: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  gingerButton: {
    position: "absolute",
    top: 432,
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
  icon2: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  labelText5: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  mushroomsButton: {
    position: "absolute",
    top: 384,
    left: 188,
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
  labelText6: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "700",
    fontFamily: "Open Sans",
    color: "#fff",
    textAlign: "center",
  },
  continueButton: {
    position: "absolute",
    top: 544,
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
  addedByYou: {
    position: "absolute",
    top: 248,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 207,
    height: 32,
  },
  icon3: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  labelText7: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  avocadoAddedButton: {
    position: "absolute",
    top: 288,
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
  icon4: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  labelText8: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  coconutAddedbutton: {
    position: "absolute",
    top: 288,
    left: 188,
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
  dislikesAddedByYou: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default DislikesAddedByYou;
