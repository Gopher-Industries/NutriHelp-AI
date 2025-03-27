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

const HealthConditions = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.healthConditions}>
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
        <Text style={styles.headline}>Health Conditions</Text>
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
      <Text style={styles.addedByYou}>Added by you</Text>
      <Text style={styles.mostCommon}>Most Common</Text>
      <TextInput
        style={styles.searchHealthTextInput}
        placeholder="Search Health Conditions"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
      <Pressable style={styles.vitaminB6Button}>
        <Image
          style={styles.icon1}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText, styles.ml8]}>
          <Text style={styles.vitaminB6}>{`Vitamin B6 `}</Text>
          <Text style={styles.deficiency}>deficiency</Text>
        </Text>
      </Pressable>
      <Pressable style={styles.limitSodiumButton}>
        <Image
          style={styles.icon2}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText1, styles.ml8]}>
          <Text style={styles.limitSodium}>Limit Sodium</Text>
          <Text style={styles.mg}>2400mg</Text>
        </Text>
      </Pressable>
      <Pressable style={styles.vitaminDDeficButton}>
        <Image
          style={styles.icon3}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText2, styles.ml8]}>
          <Text style={styles.vitaminD}>Vitamin D</Text>
          <Text style={styles.deficiency1}>deficiency</Text>
        </Text>
      </Pressable>
      <Pressable style={styles.limitCholAddedButton}>
        <Image
          style={styles.icon4}
          resizeMode="cover"
          source={require("../assets/icon12.png")}
        />
        <Text style={[styles.labelText3, styles.ml8]}>
          <Text style={styles.limit}>{`Limit `}</Text>
          <Text style={styles.cholesterol}>Cholesterol</Text>
          <Text style={styles.mg1}>2800mg</Text>
        </Text>
      </Pressable>
      <Pressable style={styles.hypertensionButton}>
        <Text style={styles.labelText4}>Hypertension</Text>
      </Pressable>
      <Pressable style={styles.diabetesType2Button}>
        <Text style={styles.labelText5}>Diabetes type 2</Text>
      </Pressable>
      <Pressable style={styles.ironDeficiencyButton}>
        <Text style={styles.labelText6}>Iron deficiency</Text>
      </Pressable>
      <Pressable style={styles.noneButton}>
        <Text style={styles.labelText7}>None</Text>
      </Pressable>
      <Pressable style={styles.heartDiseaseButton}>
        <Text style={styles.labelText8}>Heart Disease</Text>
      </Pressable>
      <Pressable style={styles.cardiovascularButton}>
        <Text style={styles.labelText9}>Cardiovascular</Text>
      </Pressable>
      <Pressable
        style={styles.continueButton}
        onPress={() => navigation.navigate("YourPreferences")}
      >
        <Text style={styles.labelText10}>Continue</Text>
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
    bottom: 584,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
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
    width: 162,
    height: 32,
  },
  mostCommon: {
    position: "absolute",
    top: 432,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 203,
    height: 32,
  },
  searchHealthTextInput: {
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
  icon1: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  vitaminB6: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  deficiency: {
    margin: 0,
  },
  labelText: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  vitaminB6Button: {
    position: "absolute",
    top: 288,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 48,
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
  limitSodium: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  mg: {
    margin: 0,
  },
  labelText1: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  limitSodiumButton: {
    position: "absolute",
    top: 352,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 64,
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
  vitaminD: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  deficiency1: {
    margin: 0,
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
  vitaminDDeficButton: {
    position: "absolute",
    top: 288,
    left: 188,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 48,
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
  limit: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  cholesterol: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  mg1: {
    margin: 0,
  },
  labelText3: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  limitCholAddedButton: {
    position: "absolute",
    top: 352,
    left: 188,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 64,
    flexDirection: "row",
    paddingLeft: 8,
    paddingTop: 6,
    paddingRight: 16,
    paddingBottom: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  labelText4: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  hypertensionButton: {
    position: "absolute",
    top: 472,
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
  labelText5: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  diabetesType2Button: {
    position: "absolute",
    top: 520,
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
  labelText6: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  ironDeficiencyButton: {
    position: "absolute",
    top: 568,
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
  labelText7: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  noneButton: {
    position: "absolute",
    top: 472,
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
  labelText8: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  heartDiseaseButton: {
    position: "absolute",
    top: 520,
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
  labelText9: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  cardiovascularButton: {
    position: "absolute",
    top: 568,
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
  labelText10: {
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
    top: 640,
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
  healthConditions: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 752,
    overflow: "hidden",
  },
});

export default HealthConditions;
