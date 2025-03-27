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

const Permissions1 = () => {
  const [cameraSwitchValue, setCameraSwitchValue] = useState(true);
  const [contactsSwitchValue, setContactsSwitchValue] = useState(true);
  const [bluetoothSwitchValue, setBluetoothSwitchValue] = useState(true);
  const navigation = useNavigation();
  const [locationSwitchValue, setLocationSwitchValue] = useState(false);
  const [healthSwitchValue, setHealthSwitchValue] = useState(false);

  return (
    <View style={styles.permissions}>
      <Text style={styles.weNeedAccessToTheFollowin}>
        We need access to the following to provide the best experience for you
      </Text>
      <Text style={styles.camera}>Camera</Text>
      <Text style={styles.location}>Location</Text>
      <Text style={styles.contacts}>Contacts</Text>
      <Text style={styles.bluetooth}>{`Bluetooth `}</Text>
      <Text style={styles.health}>Health</Text>
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
        <Text style={styles.headline}>Permissions</Text>
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
        style={styles.cameraSwitch}
        value={cameraSwitchValue}
        onValueChange={setCameraSwitchValue}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.contactsSwitch}
        value={contactsSwitchValue}
        onValueChange={setContactsSwitchValue}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Switch
        style={styles.bluetoothSwitch}
        value={bluetoothSwitchValue}
        onValueChange={setBluetoothSwitchValue}
        thumbColor="#fff"
        trackColor={{ false: "#939393", true: "#8273a9" }}
      />
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("Access")}
      >
        <Text style={styles.labelText}>Continue</Text>
      </Pressable>
      <Switch
        style={styles.locationSwitch}
        value={locationSwitchValue}
        onValueChange={setLocationSwitchValue}
        thumbColor="#79747e"
        trackColor={{ false: "#939393", true: "#e7e0ec" }}
      />
      <Switch
        style={styles.healthSwitch}
        value={healthSwitchValue}
        onValueChange={setHealthSwitchValue}
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
  weNeedAccessToTheFollowin: {
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
  camera: {
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
    width: 84,
    height: 27,
  },
  location: {
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
    width: 87,
    height: 21,
  },
  contacts: {
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
    width: 84,
    height: 27,
  },
  bluetooth: {
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
    width: 87,
    height: 31,
  },
  health: {
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
    width: 66,
    height: 31,
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
  cameraSwitch: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "36.25%",
    right: "4.44%",
    bottom: "58.75%",
    left: "81.11%",
  },
  contactsSwitch: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "53.75%",
    right: "4.44%",
    bottom: "41.25%",
    left: "81.11%",
  },
  bluetoothSwitch: {
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
  locationSwitch: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "45%",
    right: "4.44%",
    bottom: "50%",
    left: "81.11%",
  },
  healthSwitch: {
    position: "absolute",
    height: "5%",
    width: "14.44%",
    top: "71.25%",
    right: "4.44%",
    bottom: "23.75%",
    left: "81.11%",
  },
  permissions: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default Permissions1;
