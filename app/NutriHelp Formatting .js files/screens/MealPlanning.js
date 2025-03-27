import * as React from "react";
import {
  Text,
  StyleSheet,
  StatusBar,
  View,
  Pressable,
  Image,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const MealPlanning = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.mealPlanning}>
      <Text style={styles.selectWhichRecipesOurNutri}>
        <Text style={styles.selectWhichRecipes}>
          Select which recipes our nutritionist will automatically recommend
          based on your preferences and health?
        </Text>
      </Text>
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
        <Text style={styles.headline}>Meal Planning</Text>
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
      <View style={styles.inputChip}>
        <Text style={styles.labelText}>Dinner</Text>
      </View>
      <View style={styles.inputChip1}>
        <Text style={styles.labelText1}>None</Text>
      </View>
      <View style={styles.inputChip2}>
        <Text style={styles.labelText2}>Desert</Text>
      </View>
      <View style={styles.filterChip}>
        <Image
          style={styles.icon1}
          resizeMode="cover"
          source={require("../assets/icon12.png")}
        />
        <Text style={[styles.labelText3, styles.ml8]}>Lunch</Text>
      </View>
      <View style={styles.filterChip1}>
        <Image
          style={styles.icon2}
          resizeMode="cover"
          source={require("../assets/icon12.png")}
        />
        <Text style={[styles.labelText4, styles.ml8]}>Breakfast</Text>
      </View>
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("Permissions")}
      >
        <Text style={styles.labelText5}>Continue</Text>
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
  selectWhichRecipes: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  selectWhichRecipesOurNutri: {
    position: "absolute",
    top: 168,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 328,
    height: 74,
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
  inputChip: {
    position: "absolute",
    top: 336,
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
  inputChip1: {
    position: "absolute",
    top: 288,
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
  inputChip2: {
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
  icon1: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
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
  filterChip: {
    position: "absolute",
    top: 336,
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
  filterChip1: {
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
  labelText5: {
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
  mealPlanning: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default MealPlanning;
