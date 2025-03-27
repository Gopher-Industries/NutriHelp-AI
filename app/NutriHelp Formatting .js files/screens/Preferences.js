import * as React from "react";
import {
  Image,
  StyleSheet,
  Text,
  View,
  Pressable,
  StatusBar,
} from "react-native";

const Preferences = () => {
  return (
    <View style={styles.preferences}>
      <View style={styles.topAppBar}>
        <Image
          style={styles.leadingIcon}
          resizeMode="cover"
          source={require("../assets/leadingicon.png")}
        />
        <Text style={styles.headline}>Preferences</Text>
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
      <View style={styles.surfaceAt1} />
      <View style={styles.surfaceAt11} />
      <View style={styles.surfaceAt12} />
      <View style={styles.surfaceAt13} />
      <View style={styles.surfaceAt14} />
      <View style={styles.surfaceAt15} />
      <View style={styles.surfaceAt16} />
      <View style={styles.surfaceAt17} />
      <View style={styles.surfaceAt18} />
      <View style={styles.surfaceAt19} />
      <View style={styles.surfaceAt110} />
      <View style={styles.surfaceAt111} />
      <View style={styles.surfaceAt112} />
      <View style={styles.surfaceAt113} />
      <View style={styles.surfaceAt114} />
      <View style={styles.surfaceAt115} />
      <View style={styles.surfaceAt116} />
      <View style={styles.surfaceAt117} />
      <View style={styles.surfaceAt118} />
      <View style={styles.surfaceAt119} />
      <Text style={styles.you}>You</Text>
      <Text style={styles.about}>About</Text>
      <Text style={styles.n}>N</Text>
      <Text style={styles.account1}>
        <Text style={styles.account}>Account</Text>
      </Text>
      <Text style={styles.fAQ}>FAQ</Text>
      <Text style={styles.contactUs1}>
        <Text style={styles.contactUs}>Contact Us</Text>
      </Text>
      <Text style={styles.logout}>Logout</Text>
      <Text style={styles.informationAccess}>Information Access</Text>
      <Text style={styles.healthConditions1}>
        <Text style={styles.healthConditions}>Health Conditions</Text>
      </Text>
      <Text style={styles.allergies}>Allergies</Text>
      <Text style={styles.dietaryRequirements}>Dietary Requirements</Text>
      <Image
        style={styles.youArrowIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.aboutArrowIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.accountArrowIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.faqArrowIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.contactUsArrowIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.logoutArrowIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.infoAccessArrowButtonIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.healthConditionsArrowButtonIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.allergiesArrowButtonIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.dietaryArrowButtonIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Text style={styles.healthNutrition}>{`Health & Nutrition`}</Text>
      <Text style={styles.personalInformation}>Personal Information</Text>
      <Text style={styles.nutriHelp}>NutriHelp</Text>
      <Image
        style={styles.healthAndSafetyIcon}
        resizeMode="cover"
        source={require("../assets/health-and-safety.png")}
      />
      <Image
        style={styles.lunchDiningIcon}
        resizeMode="cover"
        source={require("../assets/lunch-dining.png")}
      />
      <Image
        style={styles.settingsIcon}
        resizeMode="cover"
        source={require("../assets/settings.png")}
      />
      <Image
        style={styles.adminPanelSettingsIcon}
        resizeMode="cover"
        source={require("../assets/admin-panel-settings.png")}
      />
      <Image
        style={styles.personIcon}
        resizeMode="cover"
        source={require("../assets/person.png")}
      />
      <Image
        style={styles.grassIcon}
        resizeMode="cover"
        source={require("../assets/grass.png")}
      />
      <Image
        style={styles.quizIcon}
        resizeMode="cover"
        source={require("../assets/quiz.png")}
      />
      <Image
        style={styles.draftsIcon}
        resizeMode="cover"
        source={require("../assets/drafts.png")}
      />
      <Image
        style={styles.logoutIcon}
        resizeMode="cover"
        source={require("../assets/logout.png")}
      />
      <Pressable style={styles.surfaceAt120} />
      <Pressable style={styles.surfaceAt121} />
      <Text style={styles.notifications}>Notifications</Text>
      <Image
        style={styles.arrowForwardIosIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications.png")}
      />
      <StatusBar barStyle="default" translucent={true} />
      <Image
        style={styles.notificationsIcon1}
        resizeMode="cover"
        source={require("../assets/notifications1.png")}
      />
      <View style={styles.navigationBar}>
        <View style={styles.segment}>
          <Image
            style={styles.icon}
            resizeMode="cover"
            source={require("../assets/icon.png")}
          />
          <Text style={[styles.labelText, styles.mt4]}>Plan</Text>
        </View>
        <View style={styles.segment1}>
          <Image
            style={styles.inactiveicon}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText1, styles.mt8]}>Groceries</Text>
        </View>
        <View style={styles.segment2}>
          <Image
            style={styles.inactiveicon1}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText2, styles.mt8]}>Unnamed</Text>
        </View>
        <View style={styles.segment3}>
          <Image
            style={styles.inactiveicon2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText3, styles.mt8]}>Preferences</Text>
        </View>
      </View>
      <Image
        style={styles.groceriesIcon}
        resizeMode="cover"
        source={require("../assets/groceries.png")}
      />
      <Image
        style={styles.planIcon}
        resizeMode="cover"
        source={require("../assets/plan.png")}
      />
      <View style={styles.button}>
        <Text style={styles.labelText4}>See All</Text>
      </View>
      <Image
        style={styles.unnamedIcon}
        resizeMode="cover"
        source={require("../assets/unnamed.png")}
      />
      <Image
        style={styles.preferencesIcon}
        resizeMode="cover"
        source={require("../assets/preferences.png")}
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
    bottom: 946,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  surfaceAt1: {
    position: "absolute",
    top: 464,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt11: {
    position: "absolute",
    top: 712,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt12: {
    position: "absolute",
    top: 528,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt13: {
    position: "absolute",
    top: 840,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt14: {
    position: "absolute",
    top: 904,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt15: {
    position: "absolute",
    top: 968,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt16: {
    position: "absolute",
    top: 592,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt17: {
    position: "absolute",
    top: 216,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt18: {
    position: "absolute",
    top: 280,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt19: {
    position: "absolute",
    top: 344,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt110: {
    position: "absolute",
    top: 217,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt111: {
    position: "absolute",
    top: 281,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt112: {
    position: "absolute",
    top: 345,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt113: {
    position: "absolute",
    top: 465,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt114: {
    position: "absolute",
    top: 529,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt115: {
    position: "absolute",
    top: 593,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt116: {
    position: "absolute",
    top: 713,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt117: {
    position: "absolute",
    top: 841,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt118: {
    position: "absolute",
    top: 905,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  surfaceAt119: {
    position: "absolute",
    top: 969,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  you: {
    position: "absolute",
    top: 476,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  about: {
    position: "absolute",
    top: 724,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  n: {
    position: "absolute",
    top: 724,
    left: 34,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    width: 15,
    height: 24,
  },
  account: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  account1: {
    position: "absolute",
    top: 540,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  fAQ: {
    position: "absolute",
    top: 852,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  contactUs: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  contactUs1: {
    position: "absolute",
    top: 916,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  logout: {
    position: "absolute",
    top: 980,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  informationAccess: {
    position: "absolute",
    top: 604,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 166,
    height: 24,
  },
  healthConditions: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  healthConditions1: {
    position: "absolute",
    top: 228,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  allergies: {
    position: "absolute",
    top: 292,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  dietaryRequirements: {
    position: "absolute",
    top: 356,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 183,
    height: 24,
  },
  youArrowIcon: {
    position: "absolute",
    top: 476,
    left: 300,
    width: 24,
    height: 24,
  },
  aboutArrowIcon: {
    position: "absolute",
    top: 724,
    left: 300,
    width: 24,
    height: 24,
  },
  accountArrowIcon: {
    position: "absolute",
    top: 540,
    left: 300,
    width: 24,
    height: 24,
  },
  faqArrowIcon: {
    position: "absolute",
    top: 852,
    left: 300,
    width: 24,
    height: 24,
  },
  contactUsArrowIcon: {
    position: "absolute",
    top: 916,
    left: 300,
    width: 24,
    height: 24,
  },
  logoutArrowIcon: {
    position: "absolute",
    top: 980,
    left: 300,
    width: 24,
    height: 24,
  },
  infoAccessArrowButtonIcon: {
    position: "absolute",
    top: 604,
    left: 300,
    width: 24,
    height: 24,
  },
  healthConditionsArrowButtonIcon: {
    position: "absolute",
    top: 228,
    left: 300,
    width: 24,
    height: 24,
  },
  allergiesArrowButtonIcon: {
    position: "absolute",
    top: 292,
    left: 300,
    width: 24,
    height: 24,
  },
  dietaryArrowButtonIcon: {
    position: "absolute",
    top: 356,
    left: 300,
    width: 24,
    height: 24,
  },
  healthNutrition: {
    position: "absolute",
    top: 178,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 223,
    height: 26,
  },
  personalInformation: {
    position: "absolute",
    top: 426,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 223,
    height: 26,
  },
  nutriHelp: {
    position: "absolute",
    top: 672,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 223,
    height: 26,
  },
  healthAndSafetyIcon: {
    position: "absolute",
    top: 228,
    left: 31,
    width: 24,
    height: 24,
  },
  lunchDiningIcon: {
    position: "absolute",
    top: 356,
    left: 31,
    width: 24,
    height: 24,
  },
  settingsIcon: {
    position: "absolute",
    top: 540,
    left: 31,
    width: 24,
    height: 24,
  },
  adminPanelSettingsIcon: {
    position: "absolute",
    top: 604,
    left: 31,
    width: 24,
    height: 24,
  },
  personIcon: {
    position: "absolute",
    top: 476,
    left: 30,
    width: 24,
    height: 24,
  },
  grassIcon: {
    position: "absolute",
    top: 290,
    left: 30,
    width: 24,
    height: 24,
  },
  quizIcon: {
    position: "absolute",
    top: 852,
    left: 30,
    width: 24,
    height: 24,
  },
  draftsIcon: {
    position: "absolute",
    top: 916,
    left: 31,
    width: 24,
    height: 24,
  },
  logoutIcon: {
    position: "absolute",
    top: 980,
    left: 31,
    width: 24,
    height: 24,
  },
  surfaceAt120: {
    position: "absolute",
    top: 776,
    left: 16,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt121: {
    position: "absolute",
    top: 777,
    left: 17,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  notifications: {
    position: "absolute",
    top: 788,
    left: 81,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  arrowForwardIosIcon: {
    position: "absolute",
    top: 788,
    left: 300,
    width: 24,
    height: 24,
  },
  notificationsIcon: {
    position: "absolute",
    top: 788,
    left: 30,
    width: 24,
    height: 24,
  },
  notificationsIcon1: {
    position: "absolute",
    top: 76,
    left: 270,
    width: 24,
    height: 24,
  },
  icon: {
    position: "relative",
    width: 64,
    height: 32,
    flexShrink: 0,
  },
  labelText: {
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
  labelText1: {
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
  labelText2: {
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
  groceriesIcon: {
    position: "absolute",
    bottom: 40,
    left: 123,
    width: 24,
    height: 24,
  },
  planIcon: {
    position: "absolute",
    bottom: 40,
    left: 33,
    width: 24,
    height: 24,
  },
  labelText4: {
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
    left: 283,
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
  unnamedIcon: {
    position: "absolute",
    bottom: 40,
    left: 213,
    width: 24,
    height: 24,
  },
  preferencesIcon: {
    position: "absolute",
    bottom: 40,
    left: 303,
    width: 24,
    height: 24,
  },
  preferences: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbff",
    flex: 1,
    width: "100%",
    height: 1114,
    overflow: "hidden",
  },
});

export default Preferences;
