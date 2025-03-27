import * as React from "react";
import {
  StatusBar,
  StyleSheet,
  View,
  Image,
  Text,
  Pressable,
  ImageBackground,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const TodaysPlan = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.todaysPlan}>
      <StatusBar barStyle="default" translucent={true} />
      <View style={styles.topAppBar}>
        <Image
          style={styles.leadingIcon}
          resizeMode="cover"
          source={require("../assets/leadingicon.png")}
        />
        <Text style={styles.headline}>Today’s Plan</Text>
        <View style={styles.trailingIcon}>
          <Image
            style={styles.trailingIcon3}
            resizeMode="cover"
            source={require("../assets/trailing-icon-3.png")}
          />
          <Image
            style={[styles.trailingIcon2, styles.ml24]}
            resizeMode="cover"
            source={require("../assets/trailing-icon-2.png")}
          />
          <Image
            style={[styles.trailingIcon1, styles.ml24]}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </View>
      </View>
      <View style={styles.lineView} />
      <Text style={styles.mealPlan}>Meal Plan</Text>
      <Text style={styles.breakfast}>Breakfast</Text>
      <Text style={styles.recommended}>Recommended</Text>
      <Text style={styles.recommended1}>Recommended</Text>
      <Text style={styles.recommended2}>Recommended</Text>
      <Text style={styles.recommended3}>Recommended</Text>
      <Text style={styles.kJ}>1532 - 1930 KJ</Text>
      <Text style={styles.kJ1}>1836 KJ</Text>
      <Text style={styles.kJ2}>890 KJ</Text>
      <Text style={styles.kJ3}>2274 KJ</Text>
      <Text style={styles.kJ4}>250 KJ</Text>
      <View style={styles.text}>
        <View style={styles.shape} />
      </View>
      <Pressable
        style={styles.surfaceAt1}
        onPress={() => navigation.navigate("StrawberryBananaSmoothieAdd")}
      />
      <Pressable style={styles.surfaceAt11} />
      <Pressable style={styles.surfaceAt12} />
      <Pressable style={styles.surfaceAt13} />
      <Pressable style={styles.surfaceAt14} />
      <Pressable style={styles.surfaceAt15} />
      <Pressable style={styles.surfaceAt16} />
      <Pressable style={styles.surfaceAt17} />
      <Text style={styles.strawberryBa1}>
        <Text style={styles.strawberryBa}>{`Strawberry & Ba..`}</Text>
      </Text>
      <Text style={styles.mushroomOme}>Mushroom Ome..</Text>
      <Text style={styles.pumpkinSoup}>Pumpkin Soup</Text>
      <Text style={styles.earlGreyTea}>Earl Grey Tea</Text>
      <Text style={styles.sourdoughBread}>Sourdough Bread</Text>
      <Text style={styles.oatmeal}>Oatmeal</Text>
      <Text style={styles.kJ5}>{`1153 KJ `}</Text>
      <Text style={styles.kJ6}>{`890 KJ `}</Text>
      <Text style={styles.kJ7}>{`1536 KJ `}</Text>
      <Text style={styles.kJ8}>{`250 KJ `}</Text>
      <Text style={styles.kJ9}>{`738 KJ `}</Text>
      <Text style={styles.kJ10}>{`536 KJ `}</Text>
      <Text style={styles.lunch}>Lunch</Text>
      <Text style={styles.kJ11}>1352 - 1650 KJ</Text>
      <View style={styles.text1}>
        <View style={styles.shape1} />
      </View>
      <Text style={styles.dinner}>Dinner</Text>
      <Text style={styles.kJ12}>1253 - 1920 KJ</Text>
      <View style={styles.text2}>
        <View style={styles.shape2} />
      </View>
      <Text style={styles.snacks}>Snacks</Text>
      <Text style={styles.kJ13}>432 - 800 KJ</Text>
      <View style={styles.text3}>
        <View style={styles.shape3} />
      </View>
      <Pressable style={styles.button}>
        <Text style={styles.labelText}>Today</Text>
      </Pressable>
      <Pressable
        style={styles.button1}
        onPress={() => navigation.navigate("TodaysPlanWeek")}
      >
        <Text style={styles.labelText1}>Week</Text>
      </Pressable>
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications1.png")}
      />
      <Pressable
        style={styles.surfaceAt18}
        onPress={() =>
          navigation.navigate("BottomTabsRoot", {
            screen: "NutritionReportToday",
          })
        }
      />
      <Text style={styles.viewNutritionReport}>View Nutrition Report</Text>
      <Text style={styles.health}>Health</Text>
      <Text style={styles.food}>Food</Text>
      <Text style={styles.vitamins}>Vitamins</Text>
      <Text style={styles.water}>Water</Text>
      <Image
        style={styles.addIcon}
        resizeMode="cover"
        source={require("../assets/add.png")}
      />
      <Image
        style={styles.addIcon1}
        resizeMode="cover"
        source={require("../assets/add.png")}
      />
      <ImageBackground
        style={styles.strawberrySmoothie1Of121Icon}
        resizeMode="cover"
        source={require("../assets/strawberrysmoothie1of12-11.png")}
      />
      <ImageBackground
        style={styles.iStock17857077733968717901Icon}
        resizeMode="cover"
        source={require("../assets/istock1785707773396871790-1.png")}
      />
      <ImageBackground
        style={styles.roastedPumpkinSoup83913535Icon}
        resizeMode="cover"
        source={require("../assets/roastedpumpkinsoup83913535864-1.png")}
      />
      <ImageBackground
        style={styles.simpleSourdoughBreadRecipeIcon}
        resizeMode="cover"
        source={require("../assets/simplesourdoughbreadrecipehomesteadfeature4001151677-1.png")}
      />
      <ImageBackground
        style={styles.earlGreyLeafTea200087423Icon}
        resizeMode="cover"
        source={require("../assets/earlgreyleaftea2000874-2368188992-1.png")}
      />
      <View style={styles.shape4} />
      <View style={styles.lineView1} />
      <View style={styles.shape5} />
      <View style={styles.shape6} />
      <View style={styles.shape7} />
      <View style={styles.lineView2} />
      <View style={styles.lineView3} />
      <View style={styles.lineView4} />
      <ImageBackground
        style={styles.icon}
        resizeMode="cover"
        source={require("../assets/4848007023532374350-2.png")}
      />
      <View style={styles.rectangleView} />
      <View style={styles.rectangleView1} />
      <View style={styles.rectangleView2} />
      <View style={styles.rectangleView3} />
      <View style={styles.iconButtonToggleable}>
        <Image
          style={styles.iconssettingsFilled24px}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </View>
      <View style={styles.iconButtonToggleable1}>
        <Image
          style={styles.iconssettingsFilled24px1}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </View>
      <View style={styles.lineView5} />
      <View style={styles.rectangleView4} />
      <View style={styles.rectangleView5} />
      <Image
        style={styles.checkIcon}
        resizeMode="cover"
        source={require("../assets/check.png")}
      />
      <Image
        style={styles.closeIcon}
        resizeMode="cover"
        source={require("../assets/close.png")}
      />
      <View style={styles.lineView6} />
      <View style={styles.lineView7} />
      <View style={styles.lineView8} />
      <View style={styles.lineView9} />
      <View style={styles.lineView10} />
      <View style={styles.lineView11} />
      <View style={styles.rectangleView6} />
      <View style={styles.iconButtonToggleable2}>
        <Image
          style={styles.iconssettingsFilled24px2}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </View>
      <Image
        style={styles.warningIcon}
        resizeMode="cover"
        source={require("../assets/warning.png")}
      />
      <View style={styles.rectangleView7} />
      <Pressable style={styles.iconButtonToggleable3}>
        <Image
          style={styles.iconssettingsFilled24px3}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.addIcon2}
        resizeMode="cover"
        source={require("../assets/add.png")}
      />
      <View style={styles.lineView12} />
      <View style={styles.rectangleView8} />
      <View style={styles.rectangleView9} />
      <View style={styles.iconButtonToggleable4}>
        <Image
          style={styles.iconssettingsFilled24px4}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </View>
      <Image
        style={styles.removeIcon}
        resizeMode="cover"
        source={require("../assets/remove.png")}
      />
      <Text style={styles.text4}>3 / 3</Text>
      <Image
        style={styles.jamcrownIcon}
        resizeMode="cover"
        source={require("../assets/jamcrown2.png")}
      />
      <Image
        style={styles.shoppingCartIcon}
        resizeMode="cover"
        source={require("../assets/groceries.png")}
      />
      <Image
        style={styles.restaurantIcon}
        resizeMode="cover"
        source={require("../assets/unnamed.png")}
      />
      <Image
        style={styles.accountCircleIcon}
        resizeMode="cover"
        source={require("../assets/preferences.png")}
      />
      <Image
        style={styles.calendarMonthIcon}
        resizeMode="cover"
        source={require("../assets/plan.png")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  ml24: {
    marginLeft: 24,
  },
  mt4: {
    marginTop: 4,
  },
  mt8: {
    marginTop: 8,
  },
  leadingIcon: {
    position: "absolute",
    top: 20,
    left: 16,
    width: 24,
    height: 24,
    display: "none",
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
    display: "none",
  },
  trailingIcon2: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    display: "none",
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
  },
  topAppBar: {
    position: "absolute",
    top: 56,
    bottom: 1463,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  lineView: {
    position: "absolute",
    top: 432,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  mealPlan: {
    position: "absolute",
    top: 449,
    left: 15,
    fontSize: 19,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 161,
    height: 26,
  },
  breakfast: {
    position: "absolute",
    top: 557,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 161,
    height: 26,
  },
  recommended: {
    position: "absolute",
    top: 557,
    left: 209,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 135,
    height: 26,
  },
  recommended1: {
    position: "absolute",
    top: 805,
    left: 216,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 128,
    height: 26,
  },
  recommended2: {
    position: "absolute",
    top: 1054,
    left: 210,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 134,
    height: 26,
  },
  recommended3: {
    position: "absolute",
    top: 1302,
    left: 216,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 128,
    height: 26,
  },
  kJ: {
    position: "absolute",
    top: 583,
    left: 227,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Inter",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 117,
    height: 26,
  },
  kJ1: {
    position: "absolute",
    top: 582,
    left: 106,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#b0c2a7",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 66,
    height: 26,
  },
  kJ2: {
    position: "absolute",
    top: 831,
    left: 110,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#e8bf8f",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 62,
    height: 26,
  },
  kJ3: {
    position: "absolute",
    top: 1079,
    left: 98,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#e9aaaa",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 74,
    height: 26,
  },
  kJ4: {
    position: "absolute",
    top: 1327,
    left: 110,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#e8bf8f",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 62,
    height: 26,
  },
  shape: {
    position: "absolute",
    height: "100%",
    width: "100%",
    top: "0%",
    right: "0%",
    bottom: "0%",
    left: "0%",
    borderRadius: 10,
    backgroundColor: "#eee",
  },
  text: {
    position: "absolute",
    top: 592,
    left: 16,
    width: 85,
    height: 8,
  },
  surfaceAt1: {
    position: "absolute",
    top: 624,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt11: {
    position: "absolute",
    top: 872,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt12: {
    position: "absolute",
    top: 872,
    left: 187,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt13: {
    position: "absolute",
    top: 1369,
    left: 187,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt14: {
    position: "absolute",
    top: 1120,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt15: {
    position: "absolute",
    top: 1368,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt16: {
    position: "absolute",
    top: 1120,
    left: 188,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt17: {
    position: "absolute",
    top: 624,
    left: 188,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 169,
  },
  strawberryBa: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  strawberryBa1: {
    position: "absolute",
    top: 739,
    left: 23,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 186,
    height: 24,
  },
  mushroomOme: {
    position: "absolute",
    top: 987,
    left: 23,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 178,
    height: 24,
  },
  pumpkinSoup: {
    position: "absolute",
    top: 1235,
    left: 23,
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
  earlGreyTea: {
    position: "absolute",
    top: 1486,
    left: 23,
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
  sourdoughBread: {
    position: "absolute",
    top: 1235,
    left: 195,
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
  oatmeal: {
    position: "absolute",
    top: 739,
    left: 194,
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
  kJ5: {
    position: "absolute",
    top: 763,
    left: 23,
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
  kJ6: {
    position: "absolute",
    top: 1011,
    left: 23,
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
  kJ7: {
    position: "absolute",
    top: 1259,
    left: 23,
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
  kJ8: {
    position: "absolute",
    top: 1507,
    left: 23,
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
  kJ9: {
    position: "absolute",
    top: 1259,
    left: 195,
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
  kJ10: {
    position: "absolute",
    top: 763,
    left: 194,
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
  lunch: {
    position: "absolute",
    top: 805,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 57,
    height: 26,
  },
  kJ11: {
    position: "absolute",
    top: 831,
    left: 183,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Inter",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 161,
    height: 26,
  },
  shape1: {
    position: "absolute",
    height: "100%",
    width: "100%",
    top: "0%",
    right: "0%",
    bottom: "0%",
    left: "0%",
    borderRadius: 10,
    backgroundColor: "#eee",
  },
  text1: {
    position: "absolute",
    top: 840,
    left: 16,
    width: 85,
    height: 8,
  },
  dinner: {
    position: "absolute",
    top: 1053,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 161,
    height: 26,
  },
  kJ12: {
    position: "absolute",
    top: 1079,
    left: 183,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Inter",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 161,
    height: 26,
  },
  shape2: {
    position: "absolute",
    height: "100%",
    width: "100%",
    top: "0%",
    right: "0%",
    bottom: "0%",
    left: "0%",
    borderRadius: 10,
    backgroundColor: "#eee",
  },
  text2: {
    position: "absolute",
    top: 1088,
    left: 16,
    width: 85,
    height: 8,
  },
  snacks: {
    position: "absolute",
    top: 1301,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 161,
    height: 26,
  },
  kJ13: {
    position: "absolute",
    top: 1327,
    left: 183,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Inter",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 161,
    height: 26,
  },
  shape3: {
    position: "absolute",
    height: "100%",
    width: "100%",
    top: "0%",
    right: "0%",
    bottom: "0%",
    left: "0%",
    borderRadius: 10,
    backgroundColor: "#eee",
  },
  text3: {
    position: "absolute",
    top: 1336,
    left: 16,
    width: 85,
    height: 8,
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
  button: {
    position: "absolute",
    top: 488,
    left: 16,
    borderTopLeftRadius: 100,
    borderBottomLeftRadius: 100,
    backgroundColor: "#e8def8",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 164,
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
  button1: {
    position: "absolute",
    top: 488,
    left: 179,
    borderTopRightRadius: 100,
    borderBottomRightRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 165,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  notificationsIcon: {
    position: "absolute",
    top: 76,
    left: 270,
    width: 24,
    height: 24,
  },
  surfaceAt18: {
    position: "absolute",
    top: 168,
    left: 16,
    borderRadius: 30,
    backgroundColor: "#8273a9",
    width: 328,
    height: 48,
  },
  viewNutritionReport: {
    position: "absolute",
    top: 179,
    left: 70,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#fff",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 220,
    height: 26,
  },
  health: {
    position: "absolute",
    top: 234,
    left: 19,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 64,
    height: 26,
  },
  food: {
    position: "absolute",
    top: 234,
    left: 106,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 61,
    height: 26,
  },
  vitamins: {
    position: "absolute",
    top: 234,
    left: 190,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 69,
    height: 26,
  },
  water: {
    position: "absolute",
    top: 234,
    left: 281,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 58,
    height: 26,
  },
  addIcon: {
    position: "absolute",
    height: "0.86%",
    width: "3.89%",
    top: "58.19%",
    right: "24.17%",
    bottom: "40.96%",
    left: "71.94%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  addIcon1: {
    position: "absolute",
    height: "0.86%",
    width: "3.89%",
    top: "88.66%",
    right: "24.17%",
    bottom: "10.48%",
    left: "71.94%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  strawberrySmoothie1Of121Icon: {
    position: "absolute",
    top: 625,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iStock17857077733968717901Icon: {
    position: "absolute",
    top: 873,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  roastedPumpkinSoup83913535Icon: {
    position: "absolute",
    top: 1121,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  simpleSourdoughBreadRecipeIcon: {
    position: "absolute",
    top: 1121,
    left: 189,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  earlGreyLeafTea200087423Icon: {
    position: "absolute",
    top: 1369,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  shape4: {
    position: "absolute",
    height: "0.49%",
    width: "19.72%",
    top: "36.3%",
    right: "75.83%",
    bottom: "63.21%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#b0c2a7",
  },
  lineView1: {
    position: "absolute",
    top: 593,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  shape5: {
    position: "absolute",
    height: "0.49%",
    width: "10.83%",
    top: "51.5%",
    right: "84.72%",
    bottom: "48.01%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  shape6: {
    position: "absolute",
    height: "0.49%",
    width: "23.61%",
    top: "66.71%",
    right: "71.94%",
    bottom: "32.8%",
    left: "4.44%",
    borderRadius: 10,
    backgroundColor: "#e9aaaa",
  },
  shape7: {
    position: "absolute",
    height: "0.49%",
    width: "7.22%",
    top: "81.91%",
    right: "88.33%",
    bottom: "17.6%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  lineView2: {
    position: "absolute",
    top: 841,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView3: {
    position: "absolute",
    top: 1089,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView4: {
    position: "absolute",
    top: 1337,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  icon: {
    position: "absolute",
    top: 625,
    left: 189,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  rectangleView: {
    position: "absolute",
    top: 415,
    left: 28,
    borderRadius: 30,
    backgroundColor: "#fffbfe",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 143,
    height: 46,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  rectangleView1: {
    position: "absolute",
    top: 415,
    left: 202,
    borderRadius: 30,
    backgroundColor: "#fffbfe",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 143,
    height: 46,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  rectangleView2: {
    position: "absolute",
    top: 415,
    left: 114,
    borderRadius: 30,
    backgroundColor: "#fffbfe",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 143,
    height: 46,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  rectangleView3: {
    position: "absolute",
    top: 412,
    left: 205,
    borderTopLeftRadius: 30,
    borderBottomLeftRadius: 30,
    backgroundColor: "#e9aaaa",
    width: 91,
    height: 40,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  iconssettingsFilled24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  iconButtonToggleable: {
    position: "absolute",
    marginTop: -540.5,
    top: "50%",
    left: 117,
    borderRadius: 100,
    backgroundColor: "#b0c2a7",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  iconssettingsFilled24px1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  iconButtonToggleable1: {
    position: "absolute",
    marginTop: -540.5,
    top: "50%",
    left: 31,
    borderRadius: 100,
    backgroundColor: "#e8bf8f",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  lineView5: {
    position: "absolute",
    top: 362,
    left: 117,
    borderStyle: "solid",
    borderColor: "#9a979e",
    borderTopWidth: 1,
    width: 41,
    height: 1,
  },
  rectangleView4: {
    position: "absolute",
    top: 412,
    left: 31,
    borderTopLeftRadius: 30,
    borderBottomLeftRadius: 30,
    backgroundColor: "#e8bf8f",
    width: 32,
    height: 40,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  rectangleView5: {
    position: "absolute",
    top: 412,
    left: 117,
    borderTopLeftRadius: 30,
    borderBottomLeftRadius: 30,
    backgroundColor: "#b0c2a7",
    width: 66,
    height: 40,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  checkIcon: {
    position: "absolute",
    top: 283,
    left: 125,
    width: 24,
    height: 24,
  },
  closeIcon: {
    position: "absolute",
    top: 283,
    left: 39,
    width: 24,
    height: 24,
  },
  lineView6: {
    position: "absolute",
    top: 330,
    left: 31,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 40,
    height: 1,
  },
  lineView7: {
    position: "absolute",
    top: 330,
    left: 117,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 41,
    height: 1,
  },
  lineView8: {
    position: "absolute",
    top: 330,
    left: 205,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 41,
    height: 1,
  },
  lineView9: {
    position: "absolute",
    top: 375,
    left: 44,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 15,
    height: 1,
  },
  lineView10: {
    position: "absolute",
    top: 375,
    left: 130,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 15,
    height: 1,
  },
  lineView11: {
    position: "absolute",
    top: 375,
    left: 218,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 15,
    height: 1,
  },
  rectangleView6: {
    position: "absolute",
    top: 318,
    left: 203,
    borderRadius: 30,
    backgroundColor: "#fffbfe",
    width: 45,
    height: 44,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  iconssettingsFilled24px2: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  iconButtonToggleable2: {
    position: "absolute",
    marginTop: -540.5,
    top: "50%",
    left: 205,
    borderRadius: 100,
    backgroundColor: "#e9aaaa",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  warningIcon: {
    position: "absolute",
    top: 281,
    left: 213,
    width: 24,
    height: 24,
  },
  rectangleView7: {
    position: "absolute",
    top: 415,
    left: 287,
    borderRadius: 30,
    backgroundColor: "#fffbfe",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 143,
    height: 46,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  iconssettingsFilled24px3: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  iconButtonToggleable3: {
    position: "absolute",
    marginTop: -540.5,
    top: "50%",
    left: 290,
    borderRadius: 100,
    backgroundColor: "#d1e2f2",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  addIcon2: {
    position: "absolute",
    height: "0.86%",
    width: "3.89%",
    top: "17.66%",
    right: "11.94%",
    bottom: "81.48%",
    left: "84.17%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  lineView12: {
    position: "absolute",
    top: 330,
    left: 290,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 41,
    height: 1,
  },
  rectangleView8: {
    position: "absolute",
    top: 412,
    left: 290,
    borderTopLeftRadius: 30,
    borderBottomLeftRadius: 30,
    backgroundColor: "#d1e2f2",
    width: 82,
    height: 40,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  rectangleView9: {
    position: "absolute",
    top: 414,
    left: 288,
    borderRadius: 30,
    backgroundColor: "#fff",
    width: 45,
    height: 44,
    transform: [
      {
        rotate: "-90deg",
      },
    ],
  },
  iconssettingsFilled24px4: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  iconButtonToggleable4: {
    position: "absolute",
    marginTop: -443.5,
    top: "50%",
    left: 290,
    borderRadius: 100,
    backgroundColor: "#fffbfe",
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  removeIcon: {
    position: "absolute",
    top: 380,
    left: 298,
    width: 24,
    height: 24,
  },
  text4: {
    position: "absolute",
    top: 336,
    left: 293,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 35,
    height: 26,
  },
  jamcrownIcon: {
    position: "absolute",
    top: 76,
    left: 320,
    width: 24,
    height: 24,
    overflow: "hidden",
  },
  shoppingCartIcon: {
    position: "absolute",
    bottom: 40,
    left: 123,
    width: 24,
    height: 24,
  },
  restaurantIcon: {
    position: "absolute",
    bottom: 40,
    left: 213,
    width: 24,
    height: 24,
  },
  accountCircleIcon: {
    position: "absolute",
    bottom: 40,
    left: 303,
    width: 24,
    height: 24,
  },
  calendarMonthIcon: {
    position: "absolute",
    bottom: 40,
    left: 33,
    width: 24,
    height: 24,
  },
  todaysPlan: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 1631,
    overflow: "hidden",
  },
});

export default TodaysPlan;
