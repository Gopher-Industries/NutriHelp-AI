import * as React from "react";
import {
  TextInput,
  StyleSheet,
  StatusBar,
  View,
  Pressable,
  Image,
  Text,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const Login = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.login}>
      <TextInput
        style={styles.field}
        placeholder="Password"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
      <TextInput
        style={styles.field1}
        placeholder="Email Address"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
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
        <Text style={styles.headline}>Login</Text>
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
      <View style={styles.lineView} />
      <View style={styles.lineView1} />
      <Text style={styles.or}>Or</Text>
      <Pressable
        style={styles.loginButton}
        onPress={() =>
          navigation.navigate("BottomTabsRoot", { screen: "TodaysPlan" })
        }
      >
        <Text style={styles.labelText}>Login</Text>
      </Pressable>
      <Pressable style={styles.continueGoogleButton}>
        <Text style={styles.labelText1}>Continue with Google</Text>
      </Pressable>
      <Pressable style={styles.continueFacebookButton}>
        <Text style={styles.labelText2}>Continue with Facebook</Text>
      </Pressable>
      <Text style={styles.forgotPassword}>Forgot Password?</Text>
      <View style={styles.lineView2} />
    </View>
  );
};

const styles = StyleSheet.create({
  ml24: {
    marginLeft: 24,
  },
  field: {
    position: "absolute",
    height: "8.75%",
    width: "91.11%",
    top: "38.75%",
    right: "4.44%",
    bottom: "52.5%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#49454f",
    borderWidth: 1,
  },
  field1: {
    position: "absolute",
    height: "8.75%",
    width: "91.11%",
    top: "27.5%",
    right: "4.44%",
    bottom: "63.75%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#49454f",
    borderWidth: 1,
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
  lineView: {
    position: "absolute",
    top: 441,
    left: 16,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 133,
    height: 1,
  },
  lineView1: {
    position: "absolute",
    top: 441,
    left: 212,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 133,
    height: 1,
  },
  or: {
    position: "absolute",
    top: 429,
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
  loginButton: {
    position: "absolute",
    top: 368,
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
  continueGoogleButton: {
    position: "absolute",
    top: 472,
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
  continueFacebookButton: {
    position: "absolute",
    top: 527,
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
  forgotPassword: {
    position: "absolute",
    top: 316,
    left: 197,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#79747e",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 147,
    height: 22,
  },
  lineView2: {
    position: "absolute",
    top: 340,
    left: 212,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderTopWidth: 1,
    width: 131,
    height: 1,
  },
  login: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 640,
    overflow: "hidden",
  },
});

export default Login;
