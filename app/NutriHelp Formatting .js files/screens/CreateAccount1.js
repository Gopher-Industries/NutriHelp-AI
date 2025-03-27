import * as React from "react";
import {
  StyleSheet,
  View,
  Text,
  StatusBar,
  Pressable,
  Image,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const CreateAccount1 = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.createAccount1}>
      <View style={styles.lineView} />
      <View style={styles.lineView1} />
      <Text style={styles.or}>Or</Text>
      <Text
        style={styles.getStartedByCreatingAnAcc}
      >{`Get started by creating an account `}</Text>
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
        onPress={() => navigation.navigate("CreateAccount2")}
      >
        <Text style={styles.labelText}>Continue with Email</Text>
      </Pressable>
      <Pressable style={styles.button1}>
        <Text style={styles.labelText1}>Continue with Google</Text>
      </Pressable>
      <Pressable style={styles.button2}>
        <Text style={styles.labelText2}>Continue with Facebook</Text>
      </Pressable>
    </View>
  );
};

const styles = StyleSheet.create({
  ml24: {
    marginLeft: 24,
  },
  lineView: {
    position: "absolute",
    top: 426,
    left: 16,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 133,
    height: 1,
  },
  lineView1: {
    position: "absolute",
    top: 426,
    left: 212,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 133,
    height: 1,
  },
  or: {
    position: "absolute",
    top: 414,
    left: 167,
    fontSize: 16,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#79747e",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 26,
    height: 24,
  },
  getStartedByCreatingAnAcc: {
    position: "absolute",
    top: 176,
    left: 16,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 274,
    height: 40,
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
    top: 337,
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
  labelText1: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "700",
    fontFamily: "Open Sans",
    color: "#8273a9",
    textAlign: "center",
  },
  button1: {
    position: "absolute",
    top: 473,
    left: 16,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
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
    fontWeight: "700",
    fontFamily: "Open Sans",
    color: "#8273a9",
    textAlign: "center",
  },
  button2: {
    position: "absolute",
    top: 528,
    left: 16,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  createAccount1: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default CreateAccount1;
