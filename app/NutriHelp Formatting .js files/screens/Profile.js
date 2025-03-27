import * as React from "react";
import { useState } from "react";
import {
  Pressable,
  Text,
  StyleSheet,
  TextInput,
  View,
  Image,
  StatusBar,
} from "react-native";
import { useNavigation } from "@react-navigation/native";
import DropDownPicker from "react-native-dropdown-picker";

const Profile = () => {
  const [mobilityOpen, setMobilityOpen] = useState(false);
  const [mobilityValue, setMobilityValue] = useState("");
  const [mobilityItems, setMobilityItems] = useState([
    { value: "High", label: "High" },
    { value: "Reduced", label: "Reduced" },
    { value: "Limited", label: "Limited" },
  ]);
  const [genderOpen, setGenderOpen] = useState(false);
  const [genderValue, setGenderValue] = useState("");
  const [genderItems, setGenderItems] = useState([
    { value: "Male", label: "Male" },
    { value: "Female", label: "Female" },
    { value: "Non-Binary", label: "Non-Binary" },
    { value: "Prefer Not To Say", label: "Prefer Not To Say" },
  ]);
  const navigation = useNavigation();

  return (
    <View style={styles.profile}>
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("DietaryRequirementsAddedByYou")}
      >
        <Text style={styles.labelText}>Continue</Text>
      </Pressable>
      <Text style={styles.mandatoryInformation}>*Mandatory information</Text>
      <View style={styles.mobility}>
        <DropDownPicker
          style={styles.dropDownPicker}
          open={mobilityOpen}
          setOpen={setMobilityOpen}
          value={mobilityValue}
          setValue={setMobilityValue}
          placeholder="Mobility*"
          items={mobilityItems}
          labelStyle={styles.mobilityValue}
          dropDownContainerStyle={styles.mobilitydropDownContainer}
        />
      </View>
      <TextInput
        style={styles.height}
        placeholder="Height*"
        keyboardType="number-pad"
        placeholderTextColor="#79747e"
      />
      <TextInput
        style={styles.weight}
        placeholder="Weight*"
        keyboardType="number-pad"
        placeholderTextColor="#79747e"
      />
      <View style={styles.gender}>
        <DropDownPicker
          style={styles.dropDownPicker1}
          open={genderOpen}
          setOpen={setGenderOpen}
          value={genderValue}
          setValue={setGenderValue}
          placeholder="Gender*"
          items={genderItems}
          labelStyle={styles.genderValue}
          dropDownContainerStyle={styles.genderdropDownContainer}
        />
      </View>
      <TextInput
        style={styles.age}
        placeholder="Age*"
        keyboardType="numeric"
        placeholderTextColor="#79747e"
      />
      <TextInput
        style={styles.surname}
        placeholder="Surname*"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
      <TextInput
        style={styles.firstName}
        placeholder="First Name*"
        keyboardType="default"
        placeholderTextColor="#79747e"
      />
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
        <Text style={styles.headline}>Profile</Text>
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
      <StatusBar barStyle="default" translucent={true} />
    </View>
  );
};

const styles = StyleSheet.create({
  mobilityValue: {
    color: "#79747e",
    fontSize: 16,
    fontFamily: "Open Sans",
  },
  mobilitydropDownContainer: {
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  genderValue: {
    color: "#79747e",
    fontSize: 16,
    fontFamily: "Open Sans",
  },
  genderdropDownContainer: {
    backgroundColor: "#fff",
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  ml24: {
    marginLeft: 24,
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
    top: 712,
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
  mandatoryInformation: {
    position: "absolute",
    top: 672,
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
  dropDownPicker: {
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  mobility: {
    position: "absolute",
    height: "6.8%",
    width: "91.11%",
    top: "72.82%",
    right: "4.44%",
    bottom: "20.39%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
  },
  height: {
    position: "absolute",
    height: "6.8%",
    width: "91.11%",
    top: "64.08%",
    right: "4.44%",
    bottom: "29.13%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  weight: {
    position: "absolute",
    height: "6.8%",
    width: "91.11%",
    top: "55.34%",
    right: "4.44%",
    bottom: "37.86%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  dropDownPicker1: {
    backgroundColor: "#fff",
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  gender: {
    position: "absolute",
    height: "6.8%",
    width: "91.11%",
    top: "46.6%",
    right: "4.44%",
    bottom: "46.6%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
  },
  age: {
    position: "absolute",
    height: "6.8%",
    width: "91.11%",
    top: "37.86%",
    right: "4.44%",
    bottom: "55.34%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  surname: {
    position: "absolute",
    height: "6.8%",
    width: "91.11%",
    top: "29.13%",
    right: "4.44%",
    bottom: "64.08%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
  },
  firstName: {
    position: "absolute",
    height: "6.8%",
    width: "91.11%",
    top: "20.39%",
    right: "4.44%",
    bottom: "72.82%",
    left: "4.44%",
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#000",
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
    bottom: 656,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  profile: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 824,
    overflow: "hidden",
  },
});

export default Profile;
