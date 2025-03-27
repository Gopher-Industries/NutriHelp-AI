import * as React from "react";
import {
  StatusBar,
  StyleSheet,
  Text,
  Pressable,
  Image,
  View,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const YourPreferences = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.yourPreferences}>
      <StatusBar barStyle="default" translucent={true} />
      <Text style={styles.pleaseConfirmYourSelections}>
        Please confirm your selections
      </Text>
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
        <Text style={styles.headline}>Your Preferences</Text>
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
      <Text style={styles.specialDietaryRequirements}>
        Special dietary requirements
      </Text>
      <Text style={styles.allergies}>Allergies</Text>
      <Text style={styles.dislikes}>Dislikes</Text>
      <Text style={styles.healthConditions}>Health Conditions</Text>
      <View style={styles.inputChip}>
        <Text style={styles.labelText}>Dairy</Text>
        <Image
          style={[styles.trailingIcon4, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon.png")}
        />
      </View>
      <View style={styles.inputChip1}>
        <Text style={styles.labelText1}>None</Text>
        <Image
          style={[styles.trailingIcon5, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon.png")}
        />
      </View>
      <View style={styles.inputChip2}>
        <Text style={styles.labelText2}>Ginger</Text>
        <Image
          style={[styles.trailingIcon6, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon.png")}
        />
      </View>
      <View style={styles.inputChip3}>
        <Text style={styles.labelText3}>Mushrooms</Text>
        <Image
          style={[styles.trailingIcon7, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon.png")}
        />
      </View>
      <View style={styles.inputChip4}>
        <Text style={styles.labelText4}>
          <Text style={styles.vitaminB6}>{`Vitamin B6 `}</Text>
          <Text style={styles.deficiency}>deficiency</Text>
        </Text>
        <Image
          style={[styles.trailingIcon8, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon4.png")}
        />
      </View>
      <View style={styles.inputChip5}>
        <Text style={styles.labelText5}>
          <Text style={styles.vitaminD}>Vitamin D</Text>
          <Text style={styles.deficiency1}>deficiency</Text>
        </Text>
        <Image
          style={[styles.trailingIcon9, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon4.png")}
        />
      </View>
      <View style={styles.inputChip6}>
        <Text style={styles.labelText6}>
          <Text style={styles.limitSodium}>Limit Sodium</Text>
          <Text style={styles.mg}>2400mg</Text>
        </Text>
        <Image
          style={[styles.trailingIcon10, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon4.png")}
        />
      </View>
      <View style={styles.inputChip7}>
        <Text style={styles.labelText7}>
          <Text style={styles.limit}>{`Limit `}</Text>
          <Text style={styles.cholesterol}>Cholesterol</Text>
          <Text style={styles.mg1}>2800mg</Text>
        </Text>
        <Image
          style={[styles.trailingIcon11, styles.ml8]}
          resizeMode="cover"
          source={require("../assets/trailingicon.png")}
        />
      </View>
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("DailyNutritionPlan")}
      >
        <Text style={styles.labelText8}>Confirm Choices</Text>
      </Pressable>
      <Pressable
        style={styles.button1}
        onPress={() => navigation.navigate("DietaryRequirementsAddedByYou")}
      >
        <Text style={styles.labelText9}>Redo</Text>
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
  pleaseConfirmYourSelections: {
    position: "absolute",
    top: 168,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 238,
    height: 40,
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
    bottom: 712,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  specialDietaryRequirements: {
    position: "absolute",
    top: 222,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 309,
    height: 32,
  },
  allergies: {
    position: "absolute",
    top: 312,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 81,
    height: 32,
  },
  dislikes: {
    position: "absolute",
    top: 408,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 81,
    height: 32,
  },
  healthConditions: {
    position: "absolute",
    top: 504,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 214,
    height: 32,
  },
  labelText: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "right",
  },
  trailingIcon4: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip: {
    position: "absolute",
    top: 352,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
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
    color: "#1d192b",
    textAlign: "right",
  },
  trailingIcon5: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip1: {
    position: "absolute",
    top: 264,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
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
    color: "#1d192b",
    textAlign: "right",
  },
  trailingIcon6: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip2: {
    position: "absolute",
    top: 448,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
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
    color: "#1d192b",
    textAlign: "right",
  },
  trailingIcon7: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip3: {
    position: "absolute",
    top: 448,
    left: 188,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  vitaminB6: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  deficiency: {
    margin: 0,
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
  trailingIcon8: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip4: {
    position: "absolute",
    top: 544,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 48,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  vitaminD: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  deficiency1: {
    margin: 0,
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
  trailingIcon9: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip5: {
    position: "absolute",
    top: 544,
    left: 188,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 48,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  limitSodium: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  mg: {
    margin: 0,
  },
  labelText6: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  trailingIcon10: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip6: {
    position: "absolute",
    top: 608,
    left: 16,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 64,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
    alignItems: "center",
    justifyContent: "center",
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
  trailingIcon11: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
  },
  inputChip7: {
    position: "absolute",
    top: 608,
    left: 188,
    borderRadius: 8,
    backgroundColor: "#e8def8",
    width: 156,
    height: 64,
    flexDirection: "row",
    paddingLeft: 12,
    paddingTop: 6,
    paddingRight: 8,
    paddingBottom: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  labelText8: {
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
    top: 712,
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
  labelText9: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "700",
    fontFamily: "Open Sans",
    color: "#8273a9",
    textAlign: "center",
  },
  button1: {
    position: "absolute",
    top: 768,
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
  yourPreferences: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 880,
    overflow: "hidden",
  },
});

export default YourPreferences;
