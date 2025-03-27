import * as React from "react";
import { Text, StyleSheet, Image, View } from "react-native";

const TodaysPlanWeek = () => {
  return (
    <View style={styles.todaysPlanWeek}>
      <View style={styles.timeConnectionBar}>
        <Text style={styles.time}>9:30</Text>
        <Image
          style={styles.cameraCutoutIcon}
          resizeMode="cover"
          source={require("../assets/camera-cutout.png")}
        />
        <Image
          style={styles.rightIcons}
          resizeMode="cover"
          source={require("../assets/right-icons.png")}
        />
      </View>
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
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications1.png")}
      />
      <View style={styles.rectangleView} />
      <View style={styles.surfaceAt1} />
      <Text style={styles.viewNutritionReport}>View Nutrition Report</Text>
      <Text style={styles.health}>Health</Text>
      <Text style={styles.food}>Food</Text>
      <Text style={styles.vitamins}>Vitamins</Text>
      <Text style={styles.water}>Water</Text>
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
      <View style={styles.lineView1} />
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
      <View style={styles.lineView2} />
      <View style={styles.lineView3} />
      <View style={styles.lineView4} />
      <View style={styles.lineView5} />
      <View style={styles.lineView6} />
      <View style={styles.lineView7} />
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
      <Text style={styles.mon01Aug}>Mon 01 Aug</Text>
      <Image
        style={styles.arrowBackIosNewIcon}
        resizeMode="cover"
        source={require("../assets/arrow-back-ios-new.png")}
      />
      <Image
        style={styles.arrowBackIosNewIcon1}
        resizeMode="cover"
        source={require("../assets/arrow-back-ios-new1.png")}
      />
      <View style={styles.iconButton}>
        <Image
          style={styles.iconssettings24px}
          resizeMode="cover"
          source={require("../assets/iconssettings-24px19.png")}
        />
      </View>
      <Image
        style={styles.dateRangeIcon}
        resizeMode="cover"
        source={require("../assets/date-range.png")}
      />
      <View style={styles.surfaceAt11} />
      <View style={styles.surfaceAt12} />
      <View style={styles.surfaceAt13} />
      <View style={styles.surfaceAt14} />
      <View style={styles.surfaceAt15} />
      <View style={styles.surfaceAt16} />
      <Text style={styles.strawberryBa1}>
        <Text style={styles.strawberryBa}>{`Strawberry & Ba..`}</Text>
      </Text>
      <Text style={styles.mushroomOme}>Mushroom Ome..</Text>
      <Text style={styles.pumpkinSoup}>Pumpkin Soup</Text>
      <Text style={styles.earlGreyTea}>Earl Grey Tea</Text>
      <Text style={styles.sourdoughBread}>Sourdough Bread</Text>
      <Text style={styles.oatmeal}>Oatmeal</Text>
      <Text style={styles.kJ}>{`1153 KJ `}</Text>
      <Text style={styles.kJ1}>{`890 KJ `}</Text>
      <Text style={styles.kJ2}>{`1205 KJ `}</Text>
      <Text style={styles.kJ3}>{`250 KJ `}</Text>
      <Text style={styles.kJ4}>{`738 KJ `}</Text>
      <Text style={styles.kJ5}>{`536 KJ `}</Text>
      <Image
        style={styles.strawberrySmoothie1Of121Icon}
        resizeMode="cover"
        source={require("../assets/strawberrysmoothie1of12-11.png")}
      />
      <Image
        style={styles.iStock17857077733968717901Icon}
        resizeMode="cover"
        source={require("../assets/istock1785707773396871790-1.png")}
      />
      <Image
        style={styles.roastedPumpkinSoup83913535Icon}
        resizeMode="cover"
        source={require("../assets/roastedpumpkinsoup83913535864-1.png")}
      />
      <Image
        style={styles.simpleSourdoughBreadRecipeIcon}
        resizeMode="cover"
        source={require("../assets/simplesourdoughbreadrecipehomesteadfeature4001151677-1.png")}
      />
      <Image
        style={styles.earlGreyLeafTea200087423Icon}
        resizeMode="cover"
        source={require("../assets/earlgreyleaftea2000874-2368188992-1.png")}
      />
      <Image
        style={styles.icon}
        resizeMode="cover"
        source={require("../assets/4848007023532374350-2.png")}
      />
      <View style={styles.surfaceAt17} />
      <View style={styles.surfaceAt18} />
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
      <View style={styles.rectangleView7} />
      <View style={styles.iconButtonToggleable3}>
        <Image
          style={styles.iconssettingsFilled24px3}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </View>
      <Image
        style={styles.addIcon2}
        resizeMode="cover"
        source={require("../assets/add.png")}
      />
      <View style={styles.lineView8} />
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
      <Text style={styles.text}>3 / 3</Text>
      <Text style={styles.breakfast}>Breakfast</Text>
      <Text style={styles.recommended}>Recommended</Text>
      <Text style={styles.recommended1}>Recommended</Text>
      <Text style={styles.recommended2}>Recommended</Text>
      <Text style={styles.recommended3}>Recommended</Text>
      <Text style={styles.kJ6}>1532 - 1930 KJ</Text>
      <Text style={styles.kJ7}>1836 KJ</Text>
      <Text style={styles.kJ8}>890 KJ</Text>
      <Text style={styles.kJ9}>2274 KJ</Text>
      <Text style={styles.kJ10}>250 KJ</Text>
      <View style={styles.text1}>
        <View style={styles.shape} />
      </View>
      <Text style={styles.lunch}>Lunch</Text>
      <Text style={styles.kJ11}>1352 - 1650 KJ</Text>
      <View style={styles.text2}>
        <View style={styles.shape1} />
      </View>
      <Text style={styles.dinner}>Dinner</Text>
      <Text style={styles.kJ12}>1253 - 1920 KJ</Text>
      <View style={styles.text3}>
        <View style={styles.shape2} />
      </View>
      <Text style={styles.snacks}>Snacks</Text>
      <Text style={styles.kJ13}>432 - 800 KJ</Text>
      <View style={styles.text4}>
        <View style={styles.shape3} />
      </View>
      <View style={styles.shape4} />
      <View style={styles.lineView9} />
      <View style={styles.shape5} />
      <View style={styles.shape6} />
      <View style={styles.shape7} />
      <View style={styles.lineView10} />
      <View style={styles.lineView11} />
      <View style={styles.lineView12} />
      <Image
        style={styles.jamcrownIcon}
        resizeMode="cover"
        source={require("../assets/jamcrown.png")}
      />
      <View style={styles.button}>
        <Text style={styles.labelText}>Today</Text>
      </View>
      <View style={styles.button1}>
        <Text style={styles.labelText1}>Week</Text>
      </View>
      <View style={styles.navigationBar}>
        <View style={styles.segment}>
          <Image
            style={styles.icon1}
            resizeMode="cover"
            source={require("../assets/icon3.png")}
          />
          <Text style={[styles.labelText2, styles.mt4]}>Plan</Text>
        </View>
        <View style={styles.segment1}>
          <Image
            style={styles.inactiveicon}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText3, styles.mt8]}>Groceries</Text>
        </View>
        <View style={styles.segment2}>
          <Image
            style={styles.inactiveicon1}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText4, styles.mt8]}>Unnamed</Text>
        </View>
        <View style={styles.segment3}>
          <Image
            style={styles.inactiveicon2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText5, styles.mt8]}>Preferences</Text>
        </View>
      </View>
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
  time: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0.1,
    lineHeight: 20,
    fontWeight: "500",
    fontFamily: "Roboto",
    color: "#1f1f1f",
    textAlign: "left",
  },
  cameraCutoutIcon: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    display: "none",
  },
  rightIcons: {
    position: "relative",
    width: 46,
    height: 17,
    flexShrink: 0,
  },
  timeConnectionBar: {
    position: "absolute",
    top: 0,
    left: 0,
    width: 360,
    height: 52,
    overflow: "hidden",
    flexDirection: "row",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "flex-end",
    justifyContent: "space-between",
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
    bottom: 1502,
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
  notificationsIcon: {
    position: "absolute",
    top: 76,
    left: 270,
    width: 24,
    height: 24,
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
  surfaceAt1: {
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
    marginTop: -560,
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
    marginTop: -560,
    top: "50%",
    left: 31,
    borderRadius: 100,
    backgroundColor: "#e8bf8f",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  lineView1: {
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
  lineView2: {
    position: "absolute",
    top: 330,
    left: 31,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 40,
    height: 1,
  },
  lineView3: {
    position: "absolute",
    top: 330,
    left: 117,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 41,
    height: 1,
  },
  lineView4: {
    position: "absolute",
    top: 330,
    left: 205,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 41,
    height: 1,
  },
  lineView5: {
    position: "absolute",
    top: 375,
    left: 44,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 15,
    height: 1,
  },
  lineView6: {
    position: "absolute",
    top: 375,
    left: 130,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 15,
    height: 1,
  },
  lineView7: {
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
    marginTop: -560,
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
  mon01Aug: {
    position: "absolute",
    top: 557,
    left: 61,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 161,
    height: 26,
  },
  arrowBackIosNewIcon: {
    position: "absolute",
    top: 557,
    left: 10,
    width: 24,
    height: 24,
  },
  arrowBackIosNewIcon1: {
    position: "absolute",
    top: 557,
    left: 249,
    width: 24,
    height: 24,
  },
  iconssettings24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    display: "none",
  },
  iconButton: {
    position: "absolute",
    marginTop: -285,
    top: "50%",
    left: 294,
    borderRadius: 100,
    backgroundColor: "#e8def8",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  dateRangeIcon: {
    position: "absolute",
    top: 557,
    left: 302,
    width: 24,
    height: 24,
  },
  surfaceAt11: {
    position: "absolute",
    top: 672,
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
    top: 920,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt13: {
    position: "absolute",
    top: 1168,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt14: {
    position: "absolute",
    top: 1416,
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
    top: 1168,
    left: 188,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt16: {
    position: "absolute",
    top: 672,
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
    top: 788,
    left: 23,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 166,
    height: 24,
  },
  mushroomOme: {
    position: "absolute",
    top: 1035,
    left: 23,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 175,
    height: 24,
  },
  pumpkinSoup: {
    position: "absolute",
    top: 1283,
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
    top: 1532,
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
    top: 1283,
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
    top: 788,
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
  kJ: {
    position: "absolute",
    top: 811,
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
  kJ1: {
    position: "absolute",
    top: 1059,
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
  kJ2: {
    position: "absolute",
    top: 1307,
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
  kJ3: {
    position: "absolute",
    top: 1555,
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
  kJ4: {
    position: "absolute",
    top: 1307,
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
  kJ5: {
    position: "absolute",
    top: 811,
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
  strawberrySmoothie1Of121Icon: {
    position: "absolute",
    top: 673,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iStock17857077733968717901Icon: {
    position: "absolute",
    top: 921,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  roastedPumpkinSoup83913535Icon: {
    position: "absolute",
    top: 1169,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  simpleSourdoughBreadRecipeIcon: {
    position: "absolute",
    top: 1169,
    left: 189,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  earlGreyLeafTea200087423Icon: {
    position: "absolute",
    top: 1417,
    left: 17,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  icon: {
    position: "absolute",
    top: 673,
    left: 189,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  surfaceAt17: {
    position: "absolute",
    top: 920,
    left: 188,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  surfaceAt18: {
    position: "absolute",
    top: 1416,
    left: 188,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  addIcon: {
    position: "absolute",
    height: "0.84%",
    width: "3.89%",
    top: "59.7%",
    right: "23.89%",
    bottom: "39.46%",
    left: "72.22%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  addIcon1: {
    position: "absolute",
    height: "0.84%",
    width: "3.89%",
    top: "89.4%",
    right: "23.89%",
    bottom: "9.76%",
    left: "72.22%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
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
    marginTop: -560,
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
    height: "0.84%",
    width: "3.89%",
    top: "17.25%",
    right: "11.94%",
    bottom: "81.92%",
    left: "84.17%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  lineView8: {
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
    marginTop: -463,
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
  text: {
    position: "absolute",
    top: 336,
    left: 295,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 33,
    height: 26,
  },
  breakfast: {
    position: "absolute",
    top: 605,
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
    top: 605,
    left: 198,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 146,
    height: 26,
  },
  recommended1: {
    position: "absolute",
    top: 853,
    left: 204,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 140,
    height: 26,
  },
  recommended2: {
    position: "absolute",
    top: 1102,
    left: 198,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 146,
    height: 26,
  },
  recommended3: {
    position: "absolute",
    top: 1350,
    left: 203,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 141,
    height: 26,
  },
  kJ6: {
    position: "absolute",
    top: 631,
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
  kJ7: {
    position: "absolute",
    top: 630,
    left: 102,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#b0c2a7",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 70,
    height: 26,
  },
  kJ8: {
    position: "absolute",
    top: 879,
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
  kJ9: {
    position: "absolute",
    top: 1127,
    left: 99,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#e9aaaa",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 73,
    height: 26,
  },
  kJ10: {
    position: "absolute",
    top: 1375,
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
  text1: {
    position: "absolute",
    top: 640,
    left: 16,
    width: 85,
    height: 8,
  },
  lunch: {
    position: "absolute",
    top: 853,
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
    top: 879,
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
  text2: {
    position: "absolute",
    top: 888,
    left: 16,
    width: 85,
    height: 8,
  },
  dinner: {
    position: "absolute",
    top: 1101,
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
    top: 1127,
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
  text3: {
    position: "absolute",
    top: 1136,
    left: 16,
    width: 85,
    height: 8,
  },
  snacks: {
    position: "absolute",
    top: 1349,
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
    top: 1375,
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
  text4: {
    position: "absolute",
    top: 1384,
    left: 16,
    width: 85,
    height: 8,
  },
  shape4: {
    position: "absolute",
    height: "0.48%",
    width: "19.72%",
    top: "38.32%",
    right: "75.83%",
    bottom: "61.2%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#b0c2a7",
  },
  lineView9: {
    position: "absolute",
    top: 641,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  shape5: {
    position: "absolute",
    height: "0.48%",
    width: "10.83%",
    top: "53.17%",
    right: "84.72%",
    bottom: "46.35%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  shape6: {
    position: "absolute",
    height: "0.48%",
    width: "23.61%",
    top: "68.02%",
    right: "71.94%",
    bottom: "31.5%",
    left: "4.44%",
    borderRadius: 10,
    backgroundColor: "#e9aaaa",
  },
  shape7: {
    position: "absolute",
    height: "0.48%",
    width: "7.22%",
    top: "82.87%",
    right: "88.33%",
    bottom: "16.65%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  lineView10: {
    position: "absolute",
    top: 889,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView11: {
    position: "absolute",
    top: 1137,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView12: {
    position: "absolute",
    top: 1385,
    left: 69,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  jamcrownIcon: {
    position: "absolute",
    top: 76,
    left: 320,
    width: 24,
    height: 24,
    overflow: "hidden",
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
    backgroundColor: "#e8def8",
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
  icon1: {
    position: "relative",
    width: 64,
    height: 32,
    flexShrink: 0,
  },
  labelText2: {
    position: "relative",
    fontSize: 12,
    letterSpacing: 1,
    lineHeight: 16,
    fontWeight: "500",
    fontFamily: "Roboto",
    color: "#1d192b",
    textAlign: "center",
    width: 103,
  },
  segment: {
    flex: 1,
    flexDirection: "column",
    paddingHorizontal: 0,
    paddingTop: 12,
    paddingBottom: 16,
    alignItems: "center",
    justifyContent: "center",
  },
  inactiveicon: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  labelText3: {
    position: "relative",
    fontSize: 12,
    letterSpacing: 1,
    lineHeight: 16,
    fontWeight: "500",
    fontFamily: "Roboto",
    color: "#49454f",
    textAlign: "center",
    width: 103,
  },
  segment1: {
    flex: 1,
    height: 80,
    flexDirection: "column",
    paddingHorizontal: 0,
    paddingVertical: 16,
    alignItems: "center",
    justifyContent: "center",
  },
  inactiveicon1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  labelText4: {
    position: "relative",
    fontSize: 12,
    letterSpacing: 1,
    lineHeight: 16,
    fontWeight: "500",
    fontFamily: "Roboto",
    color: "#49454f",
    textAlign: "center",
    width: 103,
  },
  segment2: {
    flex: 1,
    height: 80,
    flexDirection: "column",
    paddingHorizontal: 0,
    paddingVertical: 16,
    alignItems: "center",
    justifyContent: "center",
  },
  inactiveicon2: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  labelText5: {
    position: "relative",
    fontSize: 12,
    letterSpacing: 1,
    lineHeight: 16,
    fontWeight: "500",
    fontFamily: "Roboto",
    color: "#49454f",
    textAlign: "center",
    width: 103,
  },
  segment3: {
    flex: 1,
    height: 80,
    flexDirection: "column",
    paddingHorizontal: 0,
    paddingVertical: 16,
    alignItems: "center",
    justifyContent: "center",
  },
  navigationBar: {
    position: "absolute",
    bottom: 0,
    left: 0,
    backgroundColor: "#fffbff",
    width: 360,
    flexDirection: "row",
    alignItems: "flex-start",
    justifyContent: "flex-start",
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
  todaysPlanWeek: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 1670,
    overflow: "hidden",
  },
});

export default TodaysPlanWeek;
