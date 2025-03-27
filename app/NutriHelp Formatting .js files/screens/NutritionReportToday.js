import * as React from "react";
import { Text, StyleSheet, Image, View } from "react-native";

const NutritionReportToday = () => {
  return (
    <View style={styles.nutritionReportToday}>
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
      <Text style={styles.food}>Food</Text>
      <Text style={styles.recommended}>Recommended</Text>
      <Text style={styles.max}>Max</Text>
      <Text style={styles.min}>Min</Text>
      <Text style={styles.actual}>Actual</Text>
      <Text style={styles.healthConditions}>Health Conditions</Text>
      <Text style={styles.vitamins}>Vitamins</Text>
      <Text style={styles.labelText}>5630 - 7536 KJ</Text>
      <Text style={styles.labelText1}>632 - 1220 uq</Text>
      <Text style={styles.labelText2}>1800 - 2400 mg</Text>
      <Text style={styles.labelText3}>180.3 - 230 uq</Text>
      <Text style={styles.labelText4}>20 - 45 g</Text>
      <Text style={styles.labelText5}>60.3 - 80 mg</Text>
      <Text style={styles.labelText6}>500 - 2400 mg</Text>
      <Text style={styles.labelText7}>45 - 160 mg</Text>
      <Text style={styles.labelText8}>40 - 70 g</Text>
      <Text style={styles.labelText9}>63 - 150 mg</Text>
      <Text style={styles.labelText10}>50 - 60 g</Text>
      <Text style={styles.calories}>Calories</Text>
      <Text style={styles.vitaminA}>Vitamin A</Text>
      <Text style={styles.sodium}>Sodium</Text>
      <Text style={styles.vitaminD}>Vitamin D</Text>
      <Text style={styles.protein}>{`Protein `}</Text>
      <Text style={styles.vitaminB12}>{`Vitamin B12 `}</Text>
      <Text style={styles.fat}>Fat</Text>
      <View style={styles.text}>
        <View style={styles.shape} />
      </View>
      <View style={styles.text1}>
        <View style={styles.shape1} />
      </View>
      <View style={styles.text2}>
        <View style={styles.shape2} />
      </View>
      <View style={styles.text3}>
        <View style={styles.shape3} />
      </View>
      <View style={styles.text4}>
        <View style={styles.shape4} />
      </View>
      <View style={styles.text5}>
        <View style={styles.shape5} />
      </View>
      <View style={styles.text6}>
        <View style={styles.shape6} />
      </View>
      <View style={styles.text7}>
        <View style={styles.shape7} />
      </View>
      <View style={styles.text8}>
        <View style={styles.shape8} />
      </View>
      <View style={styles.text9}>
        <View style={styles.shape9} />
      </View>
      <View style={styles.text10}>
        <View style={styles.shape10} />
      </View>
      <View style={styles.shape11} />
      <View style={styles.shape12} />
      <View style={styles.shape13} />
      <View style={styles.shape14} />
      <View style={styles.shape15} />
      <View style={styles.shape16} />
      <View style={styles.shape17} />
      <View style={styles.shape18} />
      <View style={styles.shape19} />
      <View style={styles.shape20} />
      <View style={styles.shape21} />
      <View style={styles.lineView} />
      <View style={styles.lineView1} />
      <View style={styles.lineView2} />
      <Text style={styles.carbohydrates}>Carbohydrates</Text>
      <Text style={styles.vitaminC}>Vitamin C</Text>
      <Text style={styles.cholesterol}>{`Cholesterol `}</Text>
      <Text style={styles.vitaminB6}>{`Vitamin B6 `}</Text>
      <View style={styles.topAppBar}>
        <Image
          style={styles.leadingIcon}
          resizeMode="cover"
          source={require("../assets/leadingicon.png")}
        />
        <Text style={styles.headline}>Nutrition Report</Text>
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
            source={require("../assets/trailing-icon-1.png")}
          />
        </View>
      </View>
      <View style={styles.button}>
        <Text style={styles.labelText11}>Today</Text>
      </View>
      <View style={styles.button1}>
        <Text style={styles.labelText12}>Week</Text>
      </View>
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications1.png")}
      />
      <View style={styles.lineView3} />
      <View style={styles.surfaceAt1} />
      <View style={styles.surfaceAt11} />
      <Text style={styles.sendToFamily}>Send to Family</Text>
      <Text style={styles.sendToGP}>Send to GP</Text>
      <Text style={styles.kJ}>1836 KJ</Text>
      <Text style={styles.mg}>2135 mg</Text>
      <Text style={styles.g}>22 g</Text>
      <Text style={styles.mg1}>353 mg</Text>
      <Text style={styles.uq}>1530 uq</Text>
      <Text style={styles.g1}>96 g</Text>
      <Text style={styles.uq1}>210 uq</Text>
      <Text style={styles.mg2}>58 mg</Text>
      <Text style={styles.g2}>55 g</Text>
      <Text style={styles.mg3}>127 mg</Text>
      <Text style={styles.mg4}>12 mg</Text>
      <View style={styles.lineView4} />
      <View style={styles.lineView5} />
      <View style={styles.lineView6} />
      <View style={styles.lineView7} />
      <View style={styles.lineView8} />
      <View style={styles.lineView9} />
      <View style={styles.lineView10} />
      <View style={styles.lineView11} />
      <View style={styles.lineView12} />
      <View style={styles.lineView13} />
      <View style={styles.lineView14} />
      <Text style={styles.labelText13}>2 / 3 cups</Text>
      <Text style={styles.waterIntake}>Water Intake</Text>
      <View style={styles.text11}>
        <View style={styles.shape22} />
      </View>
      <View style={styles.text12}>
        <View style={styles.shape23} />
      </View>
      <View style={styles.text13}>
        <View style={styles.shape24} />
      </View>
      <View style={styles.iconButton}>
        <Image
          style={styles.iconssettings24px}
          resizeMode="cover"
          source={require("../assets/iconssettings-24px.png")}
        />
      </View>
      <View style={styles.iconButton1}>
        <Image
          style={styles.iconssettings24px1}
          resizeMode="cover"
          source={require("../assets/iconssettings-24px.png")}
        />
      </View>
      <Image
        style={styles.removeIcon}
        resizeMode="cover"
        source={require("../assets/remove.png")}
      />
      <Image
        style={styles.addIcon}
        resizeMode="cover"
        source={require("../assets/add.png")}
      />
      <Image
        style={styles.jamcrownIcon}
        resizeMode="cover"
        source={require("../assets/jamcrown.png")}
      />
      <View style={styles.navigationBar}>
        <View style={styles.segment}>
          <Image
            style={styles.icon}
            resizeMode="cover"
            source={require("../assets/icon3.png")}
          />
          <Text style={[styles.labelText14, styles.mt4]}>Plan</Text>
        </View>
        <View style={styles.segment1}>
          <Image
            style={styles.inactiveicon}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText15, styles.mt8]}>Groceries</Text>
        </View>
        <View style={styles.segment2}>
          <Image
            style={styles.inactiveicon1}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText16, styles.mt8]}>Unnamed</Text>
        </View>
        <View style={styles.segment3}>
          <Image
            style={styles.inactiveicon2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText17, styles.mt8]}>Preferences</Text>
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
  food: {
    position: "absolute",
    top: 445,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 59,
    height: 26,
  },
  recommended: {
    position: "absolute",
    top: 445,
    left: 201,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 143,
    height: 26,
  },
  max: {
    position: "absolute",
    top: 489,
    left: 309,
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
  min: {
    position: "absolute",
    top: 489,
    left: 239,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 35,
    height: 26,
  },
  actual: {
    position: "absolute",
    top: 489,
    left: 150,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 55,
    height: 26,
  },
  healthConditions: {
    position: "absolute",
    top: 770,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 279,
    height: 26,
  },
  vitamins: {
    position: "absolute",
    top: 1074,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 279,
    height: 26,
  },
  labelText: {
    position: "absolute",
    top: "39.57%",
    left: 226,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText1: {
    position: "absolute",
    top: "83.62%",
    left: 227,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText2: {
    position: "absolute",
    top: "61.59%",
    left: 227,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText3: {
    position: "absolute",
    top: "69.71%",
    left: 227,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText4: {
    position: "absolute",
    top: "43.62%",
    left: 226,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText5: {
    position: "absolute",
    top: "87.68%",
    left: 227,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText6: {
    position: "absolute",
    top: "65.65%",
    left: 227,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText7: {
    position: "absolute",
    top: "73.77%",
    left: 227,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText8: {
    position: "absolute",
    top: "47.68%",
    left: 226,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText9: {
    position: "absolute",
    top: "91.74%",
    left: 228,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  labelText10: {
    position: "absolute",
    top: "51.74%",
    left: 226,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  calories: {
    position: "absolute",
    top: 515,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  vitaminA: {
    position: "absolute",
    top: 1123,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  sodium: {
    position: "absolute",
    top: 819,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  vitaminD: {
    position: "absolute",
    top: 931,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  protein: {
    position: "absolute",
    top: 626,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 86,
    height: 25,
  },
  vitaminB12: {
    position: "absolute",
    top: 1234,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 126,
    height: 25,
  },
  fat: {
    position: "absolute",
    top: 682,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 55,
    height: 22,
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
    top: 552,
    left: 16,
    width: 120,
    height: 8,
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
    top: 1160,
    left: 16,
    width: 120,
    height: 8,
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
    top: 856,
    left: 16,
    width: 120,
    height: 8,
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
    top: 968,
    left: 16,
    width: 120,
    height: 8,
  },
  shape4: {
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
    top: 608,
    left: 16,
    width: 120,
    height: 8,
  },
  shape5: {
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
  text5: {
    position: "absolute",
    top: 1216,
    left: 16,
    width: 120,
    height: 8,
  },
  shape6: {
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
  text6: {
    position: "absolute",
    top: 912,
    left: 16,
    width: 120,
    height: 8,
  },
  shape7: {
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
  text7: {
    position: "absolute",
    top: 1024,
    left: 16,
    width: 120,
    height: 8,
  },
  shape8: {
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
  text8: {
    position: "absolute",
    top: 664,
    left: 16,
    width: 120,
    height: 8,
  },
  shape9: {
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
  text9: {
    position: "absolute",
    top: 1272,
    left: 16,
    width: 120,
    height: 8,
  },
  shape10: {
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
  text10: {
    position: "absolute",
    top: 720,
    left: 16,
    width: 120,
    height: 8,
  },
  shape11: {
    position: "absolute",
    height: "0.58%",
    width: "17.5%",
    top: "40%",
    right: "78.06%",
    bottom: "59.42%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  shape12: {
    position: "absolute",
    height: "0.58%",
    width: "33.33%",
    top: "84.06%",
    right: "62.22%",
    bottom: "15.36%",
    left: "4.44%",
    borderRadius: 10,
    backgroundColor: "#e9aaaa",
  },
  shape13: {
    position: "absolute",
    height: "0.58%",
    width: "28.89%",
    top: "62.03%",
    right: "66.67%",
    bottom: "37.39%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#b0c2a7",
  },
  shape14: {
    position: "absolute",
    height: "0.58%",
    width: "31.94%",
    top: "70.14%",
    right: "63.61%",
    bottom: "29.28%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#b0c2a7",
  },
  shape15: {
    position: "absolute",
    height: "0.58%",
    width: "25.28%",
    top: "44.06%",
    right: "70.28%",
    bottom: "55.36%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#b0c2a7",
  },
  shape16: {
    position: "absolute",
    height: "0.58%",
    width: "20%",
    top: "88.12%",
    right: "75.56%",
    bottom: "11.3%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  shape17: {
    position: "absolute",
    height: "0.58%",
    width: "18.33%",
    top: "66.09%",
    right: "77.22%",
    bottom: "33.33%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  shape18: {
    position: "absolute",
    height: "0.58%",
    width: "27.78%",
    top: "74.2%",
    right: "67.78%",
    bottom: "25.22%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#b0c2a7",
  },
  shape19: {
    position: "absolute",
    height: "0.58%",
    width: "33.33%",
    top: "48.12%",
    right: "62.22%",
    bottom: "51.3%",
    left: "4.44%",
    borderRadius: 10,
    backgroundColor: "#e9aaaa",
  },
  shape20: {
    position: "absolute",
    height: "0.58%",
    width: "4.72%",
    top: "92.17%",
    right: "90.83%",
    bottom: "7.25%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#e8bf8f",
  },
  shape21: {
    position: "absolute",
    height: "0.58%",
    width: "28.33%",
    top: "52.17%",
    right: "67.22%",
    bottom: "47.25%",
    left: "4.44%",
    borderTopLeftRadius: 10,
    borderBottomLeftRadius: 10,
    backgroundColor: "#b0c2a7",
  },
  lineView: {
    position: "absolute",
    top: 424,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  lineView1: {
    position: "absolute",
    top: 753,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  lineView2: {
    position: "absolute",
    top: 1056,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  carbohydrates: {
    position: "absolute",
    top: 569,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 156,
    height: 27,
  },
  vitaminC: {
    position: "absolute",
    top: 1177,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 156,
    height: 27,
  },
  cholesterol: {
    position: "absolute",
    top: 873,
    left: 16,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 156,
    height: 27,
  },
  vitaminB6: {
    position: "absolute",
    top: 985,
    left: 16,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 156,
    height: 27,
  },
  leadingIcon: {
    position: "absolute",
    top: 20,
    left: 16,
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
    display: "none",
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
    bottom: 1212,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  labelText11: {
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
    top: 264,
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
  labelText12: {
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
    top: 264,
    left: 179,
    borderTopRightRadius: 100,
    borderBottomRightRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 166,
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
  lineView3: {
    position: "absolute",
    top: 240,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  surfaceAt1: {
    position: "absolute",
    top: 168,
    left: 16,
    borderRadius: 30,
    backgroundColor: "#8273a9",
    width: 156,
    height: 48,
  },
  surfaceAt11: {
    position: "absolute",
    top: 168,
    left: 188,
    borderRadius: 30,
    backgroundColor: "#e8def8",
    width: 156,
    height: 48,
  },
  sendToFamily: {
    position: "absolute",
    top: 179,
    left: 27,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#fff",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 134,
    height: 26,
  },
  sendToGP: {
    position: "absolute",
    top: 179,
    left: 199,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 134,
    height: 26,
  },
  kJ: {
    position: "absolute",
    top: 543,
    left: 126,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#e8bf8f",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 86,
    height: 26,
  },
  mg: {
    position: "absolute",
    top: 847,
    left: 131,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#b0c2a7",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 81,
    height: 26,
  },
  g: {
    position: "absolute",
    top: 599,
    left: 150,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#b0c2a7",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 62,
    height: 26,
  },
  mg1: {
    position: "absolute",
    top: 903,
    left: 150,
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
  uq: {
    position: "absolute",
    top: 1151,
    left: 119,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#e9aaaa",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 93,
    height: 26,
  },
  g1: {
    position: "absolute",
    top: 655,
    left: 150,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#e9aaaa",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 62,
    height: 26,
  },
  uq1: {
    position: "absolute",
    top: 959,
    left: 150,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#b0c2a7",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 62,
    height: 26,
  },
  mg2: {
    position: "absolute",
    top: 1207,
    left: 150,
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
  g2: {
    position: "absolute",
    top: 711,
    left: 150,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#b0c2a7",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 62,
    height: 26,
  },
  mg3: {
    position: "absolute",
    top: 1015,
    left: 150,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Inter",
    color: "#b0c2a7",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 62,
    height: 26,
  },
  mg4: {
    position: "absolute",
    top: 1263,
    left: 150,
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
  lineView4: {
    position: "absolute",
    top: 553,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView5: {
    position: "absolute",
    top: 609,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView6: {
    position: "absolute",
    top: 665,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView7: {
    position: "absolute",
    top: 721,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView8: {
    position: "absolute",
    top: 857,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView9: {
    position: "absolute",
    top: 913,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView10: {
    position: "absolute",
    top: 969,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView11: {
    position: "absolute",
    top: 1025,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView12: {
    position: "absolute",
    top: 1161,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView13: {
    position: "absolute",
    top: 1217,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  lineView14: {
    position: "absolute",
    top: 1273,
    left: 91,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderRightWidth: 1,
    width: 1,
    height: 7,
  },
  labelText13: {
    position: "absolute",
    top: "27.97%",
    left: 227,
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 118,
  },
  waterIntake: {
    position: "absolute",
    top: 337,
    left: 17,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 145,
    height: 22,
  },
  shape22: {
    position: "absolute",
    height: "100%",
    width: "100%",
    top: "0%",
    right: "0%",
    bottom: "0%",
    left: "0%",
    borderRadius: 10,
    backgroundColor: "#d1e2f2",
  },
  text11: {
    position: "absolute",
    top: 392,
    left: 16,
    width: 52,
    height: 8,
  },
  shape23: {
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
  text12: {
    position: "absolute",
    top: 392,
    left: 126,
    width: 52,
    height: 8,
  },
  shape24: {
    position: "absolute",
    height: "100%",
    width: "100%",
    top: "0%",
    right: "0%",
    bottom: "0%",
    left: "0%",
    borderRadius: 10,
    backgroundColor: "#d1e2f2",
  },
  text13: {
    position: "absolute",
    top: 392,
    left: 71,
    width: 52,
    height: 8,
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
    marginTop: -362,
    top: "50%",
    left: 304,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  iconssettings24px1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    display: "none",
  },
  iconButton1: {
    position: "absolute",
    marginTop: -362,
    top: "50%",
    left: 248,
    borderRadius: 100,
    backgroundColor: "#d1e2f2",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  removeIcon: {
    position: "absolute",
    top: 336,
    left: 312,
    width: 24,
    height: 24,
  },
  addIcon: {
    position: "absolute",
    height: "1.01%",
    width: "3.89%",
    top: "24.71%",
    right: "23.61%",
    bottom: "74.28%",
    left: "72.5%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  jamcrownIcon: {
    position: "absolute",
    top: 76,
    left: 320,
    width: 24,
    height: 24,
    overflow: "hidden",
  },
  icon: {
    position: "relative",
    width: 64,
    height: 32,
    flexShrink: 0,
  },
  labelText14: {
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
  labelText15: {
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
  labelText16: {
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
  labelText17: {
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
  nutritionReportToday: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 1380,
    overflow: "hidden",
  },
});

export default NutritionReportToday;
