import * as React from "react";
import {
  StatusBar,
  StyleSheet,
  View,
  Pressable,
  Image,
  Text,
  TextInput,
  TouchableHighlight,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const AllergiesAddedByYou = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.allergiesAddedByYou}>
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
        <Text style={styles.headline}>Allergies</Text>
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
      <TextInput
        style={styles.searchAllergiesTextInput}
        placeholder="Search Allergies"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
      <Text style={styles.mostCommon}>Most Common</Text>
      <TouchableHighlight
        style={styles.soyButton}
        underlayColor="#e8def8"
        onPress={() => {}}
      >
        <Text style={styles.labelText}>Soy</Text>
      </TouchableHighlight>
      <TouchableHighlight
        style={styles.fishButton}
        underlayColor="#e8def8"
        onPress={() => {}}
      >
        <Text style={styles.labelText1}>Fish</Text>
      </TouchableHighlight>
      <TouchableHighlight
        style={styles.glutenButton}
        underlayColor="#e8def8"
        onPress={() => {}}
      >
        <Text style={styles.labelText2}>Gluten</Text>
      </TouchableHighlight>
      <TouchableHighlight
        style={styles.noneButton}
        underlayColor="#e8def8"
        onPress={() => {}}
      >
        <Text style={styles.labelText3}>None</Text>
      </TouchableHighlight>
      <TouchableHighlight
        style={styles.eggsButton}
        underlayColor="#e8def8"
        onPress={() => {}}
      >
        <Text style={styles.labelText4}>Eggs</Text>
      </TouchableHighlight>
      <Pressable style={styles.dairyButton} onPress={() => {}}>
        <Image
          style={styles.icon1}
          resizeMode="cover"
          source={require("../assets/icon12.png")}
        />
        <Text style={[styles.labelText5, styles.ml8]}>Dairy</Text>
      </Pressable>
      <Pressable
        style={styles.continueButton}
        onPress={() => navigation.navigate("DislikesAddedByYou")}
      >
        <Text style={styles.labelText6}>Continue</Text>
      </Pressable>
      <Text style={styles.addedByYou}>Added by you</Text>
      <Pressable style={styles.treeNutsAddedButton}>
        <Image
          style={styles.icon2}
          resizeMode="cover"
          source={require("../assets/icon12.png")}
        />
        <Text style={[styles.labelText7, styles.ml8]}>Tree nuts</Text>
      </Pressable>
      <Pressable style={styles.shellfishAddedButton}>
        <Image
          style={styles.icon3}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText8, styles.ml8]}>Shellfish</Text>
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
  searchAllergiesTextInput: {
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
    width: 172,
    height: 32,
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
  soyButton: {
    position: "absolute",
    top: 384,
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
  fishButton: {
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
  glutenButton: {
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
  labelText4: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  eggsButton: {
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
  dairyButton: {
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
  icon2: {
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
  treeNutsAddedButton: {
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
  icon3: {
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
  shellfishAddedButton: {
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
  allergiesAddedByYou: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default AllergiesAddedByYou;
