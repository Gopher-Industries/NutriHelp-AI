import * as React from "react";
import { Pressable, StyleSheet, Text, Image, View } from "react-native";

const PreferenceItemView = () => {
  return (
    <View style={styles.notificationsPreferenceView}>
      <Pressable style={styles.surfaceAt1} />
      <Pressable style={styles.surfaceAt11} />
      <Text style={styles.notifications}>Notifications</Text>
      <Image
        style={styles.arrowForwardIosIcon}
        resizeMode="cover"
        source={require("../assets/youarrow.png")}
      />
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications5.png")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  surfaceAt1: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 48,
  },
  surfaceAt11: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    backgroundColor: "#fffbfe",
    width: 52,
    height: 46,
  },
  notifications: {
    position: "absolute",
    top: 12,
    left: 65,
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
    top: 12,
    left: 284,
    width: 24,
    height: 24,
  },
  notificationsIcon: {
    position: "absolute",
    top: 12,
    left: 14,
    width: 24,
    height: 24,
  },
  notificationsPreferenceView: {
    position: "absolute",
    top: 776,
    left: 16,
    width: 328,
    height: 48,
  },
});

export default PreferenceItemView;
