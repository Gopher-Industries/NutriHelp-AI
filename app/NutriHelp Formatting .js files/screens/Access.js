import * as React from "react";
import { useState } from "react";
import {
  Text,
  StyleSheet,
  TextInput,
  View,
  StatusBar,
  Pressable,
  Image,
  Switch,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const Access = () => {
  const [familyCarerSwitchValue, setFamilyCarerSwitchValue] = useState(true);
  const [weeklyReportsSwitchValue, setWeeklyReportsSwitchValue] =
    useState(true);
  const [healthReportSwitchValue, setHealthReportSwitchValue] = useState(true);
  const [groceryListSwitchValue, setGroceryListSwitchValue] = useState(false);
  const [gpSwitchValue, setGpSwitchValue] = useState(false);
  const navigation = useNavigation();

  return (
    <View style={styles.access}>
      <Text style={styles.wouldYouLikeToGiveYourFa}>
        <Text style={styles.wouldYouLike}>
          Would you like to give your Family / Carer or GP access to your
          nutritional and health information?
        </Text>
      </Text>
      <TextInput
        style={styles.textField}
        placeholder="Search contacts"
        keyboardType="default"
        placeholderTextColor="#49454f"
      />
      <Text style={styles.familyCarer}>Family / Carer</Text>
      <Text style={styles.weeklyReports}>Weekly Reports</Text>
      <Text style={styles.groceryList}>Grocery List</Text>
      <Text style={styles.healthReport}>Health Report</Text>
      <TextInput
        style={styles.textField1}
        placeholder="Search contacts"
        keyboardType="default"
        placeholderTextColor="#d0d0d0"
      />
      <Text style={styles.gP}>GP</Text>
      <View style={styles.lineView} />
      <StatusBar barStyle="default" translucent={true} />
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
        <Text style={styles.headline}>Access</Text>
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
      <Switch
        style={styles.familyCarerSwitch}
        value={familyCarerSwitchValue}
        onValueChange={setFamilyCarerSwitchValue}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.weeklyReportsSwitch}
        value={weeklyReportsSwitchValue}
        onValueChange={setWeeklyReportsSwitchValue}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.healthReportSwitch}
        value={healthReportSwitchValue}
        onValueChange={setHealthReportSwitchValue}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.groceryListSwitch}
        value={groceryListSwitchValue}
        onValueChange={setGroceryListSwitchValue}
        thumbColor="#79747e"
        trackColor={{ false: "#939393", true: "#e7e0ec" }}
      />
      <Switch
        style={styles.gpSwitch}
        value={gpSwitchValue}
        onValueChange={setGpSwitchValue}
        thumbColor="#79747e"
        trackColor={{ false: "#939393", true: "#e7e0ec" }}
      />
      <Pressable
        style={styles.continueButton}
        onPress={() => navigation.navigate("Notifications")}
      >
        <Text style={styles.labelText}>Continue</Text>
      </Pressable>
    </View>
  );
};

const styles = StyleSheet.create({
  ml24: {
    marginLeft: 24,
  },
  wouldYouLike: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  wouldYouLikeToGiveYourFa: {
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
    height: 74,
  },
  textField: {
    position: "absolute",
    top: 320,
    left: 16,
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 56,
  },
  familyCarer: {
    position: "absolute",
    top: 264,
    left: 16,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 157,
    height: 32,
  },
  weeklyReports: {
    position: "absolute",
    top: 419,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 116,
    height: 27,
  },
  groceryList: {
    position: "absolute",
    top: 475,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 105,
    height: 26,
  },
  healthReport: {
    position: "absolute",
    top: 530,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 122,
    height: 28,
  },
  textField1: {
    position: "absolute",
    top: 672,
    left: 16,
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#d0d0d0",
    borderWidth: 1,
    width: 328,
    height: 56,
  },
  gP: {
    position: "absolute",
    top: 619,
    left: 15,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 51,
    height: 25,
  },
  lineView: {
    position: "absolute",
    top: 588,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
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
    bottom: 696,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  familyCarerSwitch: {
    position: "absolute",
    height: "3.7%",
    width: "14.44%",
    top: "30.56%",
    right: "4.72%",
    bottom: "65.74%",
    left: "80.83%",
  },
  weeklyReportsSwitch: {
    position: "absolute",
    height: "3.7%",
    width: "14.44%",
    top: "48.15%",
    right: "4.72%",
    bottom: "48.15%",
    left: "80.83%",
  },
  healthReportSwitch: {
    position: "absolute",
    height: "3.7%",
    width: "14.44%",
    top: "61.11%",
    right: "4.44%",
    bottom: "35.19%",
    left: "81.11%",
  },
  groceryListSwitch: {
    position: "absolute",
    height: "3.7%",
    width: "14.44%",
    top: "54.63%",
    right: "4.44%",
    bottom: "41.67%",
    left: "81.11%",
  },
  gpSwitch: {
    position: "absolute",
    height: "3.7%",
    width: "14.44%",
    top: "71.3%",
    right: "4.44%",
    bottom: "25%",
    left: "81.11%",
  },
  labelText: {
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
    top: 752,
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
  access: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 864,
    overflow: "hidden",
  },
});

export default Access;
