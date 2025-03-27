import * as React from "react";
import {
  Text,
  StyleSheet,
  Image,
  View,
  Pressable,
  ScrollView,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const StrawberryBananaSmoothie1 = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.strawberryBananaSmoothie1}>
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
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications1.png")}
      />
      <View style={styles.topAppBar}>
        <Pressable
          style={styles.leadingIcon}
          onPress={() => navigation.goBack()}
        >
          <Image
            style={styles.icon}
            resizeMode="cover"
            source={require("../assets/leadingicon.png")}
          />
        </Pressable>
        <Text style={styles.headline}>Selection</Text>
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
      <Image
        style={styles.smoothieImageIcon}
        resizeMode="cover"
        source={require("../assets/strawberrysmoothie1of12-1.png")}
      />
      <View style={styles.swapButton}>
        <Text style={styles.labelText}>Swap</Text>
      </View>
      <Pressable style={styles.favouriteButtonCircle}>
        <Image
          style={styles.iconssettingsFilled24px}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.favouriteButtonIcon}
        resizeMode="cover"
        source={require("../assets/favorite.png")}
      />
      <Pressable style={styles.deleteButtonCircle}>
        <Image
          style={styles.iconssettingsFilled24px1}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.deleteButtonIcon}
        resizeMode="cover"
        source={require("../assets/delete.png")}
      />
      <View style={styles.servingsView}>
        <Text style={styles.servings}>Servings</Text>
        <Text style={styles.text}>1</Text>
        <Pressable style={styles.removeServingButtonCircle}>
          <Image
            style={styles.iconssettings24px}
            resizeMode="cover"
            source={require("../assets/iconssettings-24px.png")}
          />
        </Pressable>
        <Image
          style={styles.removeServingButtonIcon}
          resizeMode="cover"
          source={require("../assets/remove.png")}
        />
        <Pressable style={styles.addServingButtonCircle}>
          <Image
            style={styles.iconssettings24px1}
            resizeMode="cover"
            source={require("../assets/iconssettings-24px.png")}
          />
        </Pressable>
        <Image
          style={styles.addServingButtonIcon}
          resizeMode="cover"
          source={require("../assets/add.png")}
        />
      </View>
      <View style={styles.buttonBarView}>
        <Pressable style={styles.ingredientsButton}>
          <Text style={styles.labelText1}>Ingredients</Text>
        </Pressable>
        <Pressable style={styles.stepsButton}>
          <Text style={styles.labelText2}>Steps</Text>
        </Pressable>
        <Pressable style={styles.infoButton}>
          <Text style={styles.labelText3}>Info</Text>
        </Pressable>
      </View>
      <View style={styles.lineView} />
      <ScrollView
        style={styles.stepsView}
        showsHorizontalScrollIndicator={false}
        showsVerticalScrollIndicator={false}
      >
        <Text style={styles.steps}>Steps</Text>
        <Text style={styles.text1}>1.</Text>
        <Text style={styles.inABlenderCombineAllOfT}>
          In a blender, combine all of the ingredients; cover and process for
          30-45 seconds or until smooth. Stir if necessary. Pour into chilled
          glasses; serve immediately.
        </Text>
      </ScrollView>
      <Text style={styles.strawberryBananaSmoothie}>
        <Text
          style={styles.strawberryBanana}
        >{`Strawberry & Banana Smoothie`}</Text>
      </Text>
      <Text style={styles.kJPerServing}>1153 KJ - per serving</Text>
      <View style={styles.navigationBar}>
        <View style={styles.segment}>
          <Image
            style={styles.icon1}
            resizeMode="cover"
            source={require("../assets/icon.png")}
          />
          <Text style={[styles.labelText4, styles.mt4]}>Plan</Text>
        </View>
        <View style={styles.segment1}>
          <Image
            style={styles.inactiveicon}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText5, styles.mt8]}>Groceries</Text>
        </View>
        <View style={styles.segment2}>
          <Image
            style={styles.inactiveicon1}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText6, styles.mt8]}>Unnamed</Text>
        </View>
        <View style={styles.segment3}>
          <Image
            style={styles.inactiveicon2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText7, styles.mt8]}>Preferences</Text>
        </View>
      </View>
      <Image
        style={styles.shoppingCartIcon}
        resizeMode="cover"
        source={require("../assets/groceries.png")}
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
      <View style={styles.button}>
        <Text style={styles.labelText8}>See All</Text>
      </View>
      <Image
        style={styles.restaurantIcon}
        resizeMode="cover"
        source={require("../assets/unnamed.png")}
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
  notificationsIcon: {
    position: "absolute",
    top: 76,
    left: 270,
    width: 24,
    height: 24,
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
    bottom: 608,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  smoothieImageIcon: {
    position: "absolute",
    top: 168,
    left: 16,
    borderRadius: 9,
    width: 221,
    height: 112,
  },
  labelText: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#fff",
    textAlign: "center",
  },
  swapButton: {
    position: "absolute",
    top: 240,
    left: 252,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    width: 92,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  iconssettingsFilled24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  favouriteButtonCircle: {
    position: "absolute",
    marginTop: -219,
    top: "50%",
    left: 304,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#49454f",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  favouriteButtonIcon: {
    position: "absolute",
    top: 177,
    left: 260,
    width: 24,
    height: 24,
  },
  iconssettingsFilled24px1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  deleteButtonCircle: {
    position: "absolute",
    marginTop: -220,
    top: "50%",
    left: 252,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#49454f",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  deleteButtonIcon: {
    position: "absolute",
    top: 177,
    left: 312,
    width: 24,
    height: 24,
  },
  servings: {
    position: "absolute",
    top: 8,
    left: 0,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 69,
    height: 24,
  },
  text: {
    position: "absolute",
    top: 8,
    left: 252,
    fontSize: 19,
    letterSpacing: -0.2,
    lineHeight: 29,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 18,
    height: 24,
  },
  iconssettings24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    display: "none",
  },
  removeServingButtonCircle: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 287,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  removeServingButtonIcon: {
    position: "absolute",
    top: 8,
    left: 295,
    width: 24,
    height: 24,
  },
  iconssettings24px1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    display: "none",
  },
  addServingButtonCircle: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 195,
    borderRadius: 100,
    backgroundColor: "#e8def8",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  addServingButtonIcon: {
    position: "absolute",
    height: "35%",
    width: "4.28%",
    top: "32.5%",
    right: "32.11%",
    bottom: "32.5%",
    left: "63.61%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  servingsView: {
    position: "absolute",
    top: 344,
    left: 17,
    width: 327,
    height: 40,
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
  ingredientsButton: {
    position: "absolute",
    top: 0,
    left: 0,
    borderTopLeftRadius: 100,
    borderBottomLeftRadius: 100,
    backgroundColor: "#fffbfe",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 109,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
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
  stepsButton: {
    position: "absolute",
    top: 0,
    left: 108,
    backgroundColor: "#e8def8",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 112,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
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
  infoButton: {
    position: "absolute",
    top: 0,
    left: 219,
    borderTopRightRadius: 100,
    borderBottomRightRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 109,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  buttonBarView: {
    position: "absolute",
    top: 432,
    left: 16,
    width: 328,
    height: 40,
  },
  lineView: {
    position: "absolute",
    top: 408,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  steps: {
    position: "absolute",
    top: 0,
    left: 0,
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
  text1: {
    position: "absolute",
    top: 52,
    left: 0,
    fontSize: 19,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 59,
    height: 26,
  },
  inABlenderCombineAllOfT: {
    position: "absolute",
    top: 31,
    left: 32,
    fontSize: 16,
    lineHeight: 26,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 296,
    height: 170,
  },
  stepsView: {
    position: "absolute",
    top: 498,
    left: 16,
    width: 328,
    flex: 1,
    maxWidth: 328,
  },
  strawberryBanana: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  strawberryBananaSmoothie: {
    position: "absolute",
    top: 290,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 247,
    height: 24,
  },
  kJPerServing: {
    position: "absolute",
    top: 316,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 163,
    height: 26,
  },
  icon1: {
    position: "relative",
    width: 64,
    height: 32,
    flexShrink: 0,
  },
  labelText4: {
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
  labelText6: {
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
  labelText7: {
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
  labelText8: {
    position: "relative",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "500",
    fontFamily: "Roboto",
    color: "#1d192b",
    textAlign: "center",
    display: "none",
  },
  button: {
    position: "absolute",
    bottom: 36,
    left: 193,
    borderRadius: 100,
    backgroundColor: "#e7dff0",
    width: 64,
    height: 32,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  restaurantIcon: {
    position: "absolute",
    bottom: 40,
    left: 213,
    width: 24,
    height: 24,
  },
  strawberryBananaSmoothie1: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 776,
    overflow: "hidden",
  },
});

export default StrawberryBananaSmoothie1;
