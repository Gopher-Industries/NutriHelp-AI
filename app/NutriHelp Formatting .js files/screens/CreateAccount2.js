import * as React from "react";
import {
  TextInput,
  StyleSheet,
  Text,
  StatusBar,
  View,
  Pressable,
  Image,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const CreateAccount2 = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.createAccount2}>
      <TextInput
        style={styles.confirmEmailField}
        placeholder="Confirm Email Address*"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
      <TextInput
        style={styles.passwordField}
        placeholder="Password*"
        keyboardType="default"
        secureTextEntry
        placeholderTextColor="#79747e"
      />
      <TextInput
        style={styles.confirmPasswordField}
        placeholder="Confirm Password*"
        keyboardType="default"
        secureTextEntry
        placeholderTextColor="#79747e"
      />
      <TextInput
        style={styles.emailField}
        placeholder="Email Address*"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
      <Text style={styles.mandatoryInformation}>*Mandatory information</Text>
      <Text style={styles.passwordMustHave}>Password must have...</Text>
      <StatusBar barStyle="default" translucent={true} />
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
        <Text style={styles.headline}>{`Create Account  `}</Text>
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
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("Profile")}
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
  confirmEmailField: {
    position: "absolute",
    height: "8.75%",
    width: "91.11%",
    top: "37.5%",
    right: "4.44%",
    bottom: "53.75%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  passwordField: {
    position: "absolute",
    height: "8.75%",
    width: "91.11%",
    top: "48.75%",
    right: "4.44%",
    bottom: "42.5%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  confirmPasswordField: {
    position: "absolute",
    height: "8.75%",
    width: "91.11%",
    top: "63.75%",
    right: "4.44%",
    bottom: "27.5%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  emailField: {
    position: "absolute",
    height: "8.75%",
    width: "91.11%",
    top: "26.25%",
    right: "4.44%",
    bottom: "65%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  mandatoryInformation: {
    position: "absolute",
    top: 480,
    left: 16,
    fontSize: 16,
    letterSpacing: 1,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 221,
    height: 14,
  },
  passwordMustHave: {
    position: "absolute",
    top: 381,
    left: 16,
    fontSize: 16,
    letterSpacing: 1,
    lineHeight: 24,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 221,
    height: 14,
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
    color: "#1c1b1f",
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
  createAccount2: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default CreateAccount2;
