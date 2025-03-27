import * as React from "react";
import { useState } from "react";
import {
  Text,
  StyleSheet,
  StatusBar,
  View,
  Pressable,
  Image,
  Switch,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const Notifications = () => {
  const [notificationSwitch1Value, setNotificationSwitch1Value] =
    useState(false);
  const [notificationSwitch3Value, setNotificationSwitch3Value] =
    useState(false);
  const [notificationSwitch4Value, setNotificationSwitch4Value] =
    useState(true);
  const navigation = useNavigation();
  const [notificationSwitch2Value, setNotificationSwitch2Value] =
    useState(false);
  const [notificationSwitch5Value, setNotificationSwitch5Value] =
    useState(false);

  return (
    <View style={styles.notifications}>
      <Text style={styles.wouldYouLikeUsToSendYou}>
        <Text style={styles.wouldYouLike}>
          Would you like us to send you reminders throughout the day?
        </Text>
        <Text style={styles.blankLine}> </Text>
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
            source={require("../assets/leadingicon.png")}
          />
        </Pressable>
        <Text style={styles.headline}>Notifications</Text>
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
      <Text style={styles.notification}>Notification</Text>
      <Text style={styles.notification1}>Notification</Text>
      <Text style={styles.notification2}>Notification</Text>
      <Text style={styles.notification3}>Notification</Text>
      <Text style={styles.notification4}>Notification</Text>
      <Switch
        style={styles.notificationSwitch1}
        value={notificationSwitch1Value}
        onValueChange={setNotificationSwitch1Value}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.notificationSwitch3}
        value={notificationSwitch3Value}
        onValueChange={setNotificationSwitch3Value}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.notificationSwitch4}
        value={notificationSwitch4Value}
        onValueChange={setNotificationSwitch4Value}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Pressable
        style={styles.continueButton}
        onPress={() =>
          navigation.navigate("BottomTabsRoot", { screen: "TodaysPlan" })
        }
      >
        <Text style={styles.labelText}>Continue</Text>
      </Pressable>
      <Switch
        style={styles.notificationSwitch2}
        value={notificationSwitch2Value}
        onValueChange={setNotificationSwitch2Value}
        thumbColor="#79747e"
        trackColor={{ false: "#939393", true: "#e7e0ec" }}
      />
      <Switch
        style={styles.notificationSwitch5}
        value={notificationSwitch5Value}
        onValueChange={setNotificationSwitch5Value}
        thumbColor="#79747e"
        trackColor={{ false: "#939393", true: "#e7e0ec" }}
      />
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
  blankLine: {
    margin: 0,
  },
  wouldYouLikeUsToSendYou: {
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
    height: 49,
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
  notification: {
    position: "absolute",
    top: 232,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 123,
    height: 27,
  },
  notification1: {
    position: "absolute",
    top: 291,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 114,
    height: 21,
  },
  notification2: {
    position: "absolute",
    top: 343,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 118,
    height: 27,
  },
  notification3: {
    position: "absolute",
    top: 401,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 181,
    height: 31,
  },
  notification4: {
    position: "absolute",
    top: 457,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 167,
    height: 31,
  },
  notificationSwitch1: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "36.25%",
    right: "4.44%",
    bottom: "58.75%",
    left: "81.11%",
  },
  notificationSwitch3: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "53.75%",
    right: "4.44%",
    bottom: "41.25%",
    left: "81.11%",
  },
  notificationSwitch4: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "62.5%",
    right: "4.44%",
    bottom: "32.5%",
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
  notificationSwitch2: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "45%",
    right: "4.44%",
    bottom: "50%",
    left: "81.11%",
  },
  notificationSwitch5: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "71.25%",
    right: "4.44%",
    bottom: "23.75%",
    left: "81.11%",
  },
  notifications: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default Notifications;
