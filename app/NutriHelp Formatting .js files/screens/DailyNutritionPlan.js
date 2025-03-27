import * as React from "react";
import {
  StatusBar,
  StyleSheet,
  Text,
  View,
  Pressable,
  Image,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const DailyNutritionPlan = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.dailyNutritionPlan}>
      <StatusBar barStyle="default" translucent={true} />
      <Text style={styles.calories}>Calories</Text>
      <Text style={styles.kj}>7536 kj</Text>
      <Text style={styles.atLeast45g}>at least 45g</Text>
      <Text style={styles.atLeast70g}>at least 70g</Text>
      <Text style={styles.atLeast60g}>at least 60g</Text>
      <Text style={styles.atLeast3Cups}>at least 3 cups</Text>
      <Text style={styles.carbohydrates}>Carbohydrates</Text>
      <Text style={styles.protein}>{`Protein `}</Text>
      <Text style={styles.fat}>Fat</Text>
      <Text style={styles.water}>Water</Text>
      <View style={styles.lineView} />
      <View style={styles.lineView1} />
      <View style={styles.lineView2} />
      <View style={styles.lineView3} />
      <View style={styles.lineView4} />
      <Text style={styles.thisIsYourRecommendedDaily}>
        <Text style={styles.thisIsYour}>
          This is your recommended daily intake based on your preferences and
          health
        </Text>
      </Text>
      <Text style={styles.weWillSelectFoodsInYourM}>
        <Text style={styles.weWillSelectContainer}>
          <Text style={styles.weWillSelect}>
            We will select foods in your meal plan that are rich in the
            following vitamins.
          </Text>
        </Text>
      </Text>
      <Text style={styles.weWillSelectFoodsInYourM1}>
        <Text style={styles.weWillSelectContainer1}>
          <Text style={styles.weWillSelect1}>
            We will select foods in your meal plan that keep you within your set
            limits.
          </Text>
        </Text>
      </Text>
      <Text style={styles.healthConditions}>Health Conditions</Text>
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
        <Text style={styles.headline}>Daily Nutrition Plan</Text>
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
      <View style={styles.filterChip}>
        <Image
          style={styles.icon1}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText, styles.ml8]}>Vitamin B6</Text>
      </View>
      <View style={styles.filterChip1}>
        <Image
          style={styles.icon2}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText1, styles.ml8]}>Vitamin D</Text>
      </View>
      <View style={styles.filterChip2}>
        <Image
          style={styles.icon3}
          resizeMode="cover"
          source={require("../assets/icon9.png")}
        />
        <Text style={[styles.labelText2, styles.ml8]}>
          <Text style={styles.limitSodium}>Limit Sodium</Text>
          <Text style={styles.mg}>2400mg</Text>
        </Text>
      </View>
      <View style={styles.filterChip3}>
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
      </View>
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("MealPlanning")}
      >
        <Text style={styles.labelText4}>Continue</Text>
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
  calories: {
    position: "absolute",
    top: 254,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 74,
    height: 24,
  },
  kj: {
    position: "absolute",
    top: 252,
    left: 277,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#6750a4",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 67,
    height: 28,
  },
  atLeast45g: {
    position: "absolute",
    top: 299,
    left: 188,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#6750a4",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 156,
    height: 28,
  },
  atLeast70g: {
    position: "absolute",
    top: 347,
    left: 213,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#6750a4",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 131,
    height: 28,
  },
  atLeast60g: {
    position: "absolute",
    top: 395,
    left: 215,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#6750a4",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 129,
    height: 28,
  },
  atLeast3Cups: {
    position: "absolute",
    top: 443,
    left: 185,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#6750a4",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 159,
    height: 29,
  },
  carbohydrates: {
    position: "absolute",
    top: 293,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 156,
    height: 40,
  },
  protein: {
    position: "absolute",
    top: 345,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 70,
    height: 29,
  },
  fat: {
    position: "absolute",
    top: 395,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 55,
    height: 28,
  },
  water: {
    position: "absolute",
    top: 443,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 78,
    height: 29,
  },
  lineView: {
    position: "absolute",
    top: 289,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  lineView1: {
    position: "absolute",
    top: 337,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  lineView2: {
    position: "absolute",
    top: 385,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  lineView3: {
    position: "absolute",
    top: 433,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  lineView4: {
    position: "absolute",
    top: 480,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  thisIsYour: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  thisIsYourRecommendedDaily: {
    position: "absolute",
    top: 168,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 329,
    height: 54,
  },
  weWillSelect: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  weWillSelectContainer: {
    lineBreak: "anywhere",
    width: "100%",
  },
  weWillSelectFoodsInYourM: {
    position: "absolute",
    top: 552,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 328,
    height: 64,
  },
  weWillSelect1: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  weWillSelectContainer1: {
    lineBreak: "anywhere",
    width: "100%",
  },
  weWillSelectFoodsInYourM1: {
    position: "absolute",
    top: 668,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 328,
    height: 68,
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
    width: 225,
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
    bottom: 776,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  icon1: {
    position: "relative",
    width: 18,
    height: 18,
    flexShrink: 0,
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
  filterChip: {
    position: "absolute",
    top: 616,
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
  filterChip1: {
    position: "absolute",
    top: 616,
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
  icon3: {
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
  filterChip2: {
    position: "absolute",
    top: 736,
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
  filterChip3: {
    position: "absolute",
    top: 736,
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
    top: 832,
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
  dailyNutritionPlan: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 944,
    overflow: "hidden",
  },
});

export default DailyNutritionPlan;
