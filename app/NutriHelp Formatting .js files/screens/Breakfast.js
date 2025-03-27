import * as React from "react";
import {
  Text,
  StyleSheet,
  Image,
  View,
  Pressable,
  TextInput,
  ImageBackground,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const Breakfast = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.breakfast}>
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
      <View style={styles.topAppBar}>
        <Pressable
          style={styles.backButton}
          onPress={() => navigation.goBack()}
        >
          <Image
            style={styles.icon}
            resizeMode="cover"
            source={require("../assets/leadingicon.png")}
          />
        </Pressable>
        <Text style={styles.breakfastHeadline}>Breakfast</Text>
        <Pressable style={styles.trailingIcon}>
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
        </Pressable>
      </View>
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications1.png")}
      />
      <TextInput
        style={styles.searchTextInput}
        placeholder="Search"
        keyboardType="default"
        placeholderTextColor="#49454f"
      />
      <Pressable style={styles.createButton}>
        <Text style={styles.labelText}>Create</Text>
      </Pressable>
      <View style={styles.lineView} />
      <View style={styles.smoothieView}>
        <View style={styles.smoothieBorderView} />
        <Text style={styles.strawberryBa1}>
          <Text style={styles.strawberryBa}>{`Strawberry & Ba..`}</Text>
        </Text>
        <Text style={styles.kJ}>{`1153 KJ `}</Text>
        <ImageBackground
          style={styles.smoothieImageIcon}
          resizeMode="cover"
          source={require("../assets/strawberrysmoothie1of12-11.png")}
        />
        <Pressable style={styles.smoothieAddButtonCircle}>
          <Image
            style={styles.iconssettingsFilled24px}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.smoothieAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
      </View>
      <View style={styles.oatmealView}>
        <View style={styles.oatmealBorderView} />
        <Text style={styles.oatmeal}>Oatmeal</Text>
        <Text style={styles.kJ1}>{`536 KJ `}</Text>
        <ImageBackground
          style={styles.oatmealImageIcon}
          resizeMode="cover"
          source={require("../assets/4848007023532374350-2.png")}
        />
        <Pressable style={styles.oatmealAddButtonCircle}>
          <Image
            style={styles.iconssettingsFilled24px1}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.oatmealAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
      </View>
      <View style={styles.omeletteView}>
        <View style={styles.omeletteBorderView} />
        <Text style={styles.mushroomOme}>Mushroom Ome..</Text>
        <Text style={styles.kJ2}>{`890 KJ `}</Text>
        <ImageBackground
          style={styles.omeletteImageIcon}
          resizeMode="cover"
          source={require("../assets/istock1785707773396871790-1.png")}
        />
        <Pressable style={styles.omeletteAddButtonCircle}>
          <Image
            style={styles.iconssettingsFilled24px2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.omeletteAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
      </View>
      <View style={styles.soupView}>
        <View style={styles.soupBorderView} />
        <Text style={styles.pumpkinSoup}>Pumpkin Soup</Text>
        <Text style={styles.kJ3}>{`1205 KJ `}</Text>
        <ImageBackground
          style={styles.soupImageIcon}
          resizeMode="cover"
          source={require("../assets/roastedpumpkinsoup83913535864-1.png")}
        />
        <Pressable style={styles.soupAddButtonCircle}>
          <Image
            style={styles.iconssettingsFilled24px3}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.soupAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
      </View>
      <View style={styles.breadView}>
        <View style={styles.breadBorderView} />
        <Text style={styles.sourdoughBread}>Sourdough Bread</Text>
        <ImageBackground
          style={styles.breadImageIcon}
          resizeMode="cover"
          source={require("../assets/simplesourdoughbreadrecipehomesteadfeature4001151677-1.png")}
        />
        <Pressable style={styles.breadAddButtonCircle}>
          <Image
            style={styles.iconssettingsFilled24px4}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Text style={styles.kJ4}>{`738 KJ `}</Text>
        <Image
          style={styles.breadAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
      </View>
      <View style={styles.teaView}>
        <View style={styles.teaBorderView} />
        <Text style={styles.earlGreyTea}>Earl Grey Tea</Text>
        <Text style={styles.kJ5}>{`250 KJ `}</Text>
        <ImageBackground
          style={styles.teaImageIcon}
          resizeMode="cover"
          source={require("../assets/earlgreyleaftea2000874-2368188992-1.png")}
        />
        <Pressable style={styles.teaAddButtonCircle}>
          <Image
            style={styles.iconssettingsFilled24px5}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.teaAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
      </View>
      <View style={styles.tomatoSaladBorderView} />
      <Text style={styles.tomatoSalad}>Tomato Salad</Text>
      <Text style={styles.kJ6}>{`630 KJ `}</Text>
      <ImageBackground
        style={styles.tomatoSaladImageIcon}
        resizeMode="cover"
        source={require("../assets/tomatosaladimage.png")}
      />
      <Pressable style={styles.tomatoSaladAddButtonCircle}>
        <Image
          style={styles.iconssettingsFilled24px6}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.tomatoSaladAddButtonIcon}
        resizeMode="cover"
        source={require("../assets/bananaaddbutton.png")}
      />
      <View style={styles.tiramisuView}>
        <Text style={styles.tiramisu}>Tiramisu</Text>
        <View style={styles.tiramisuBoxView} />
        <ImageBackground
          style={styles.tiramisuImageIcon}
          resizeMode="cover"
          source={require("../assets/tiramisuimage.png")}
        />
        <Pressable style={styles.tiramisuAddButtonBorder}>
          <Image
            style={styles.iconssettingsFilled24px7}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.tiramisuAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
        <Text style={styles.kJ7}>{`1530 KJ `}</Text>
      </View>
      <Pressable style={styles.tuneButtonIcon}>
        <Image
          style={styles.iconssettingsFilled24px8}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.tuneButtonIcon1}
        resizeMode="cover"
        source={require("../assets/tune.png")}
      />
      <Text style={styles.filterAll1}>
        <Text style={styles.filterAllTxtContainer}>
          <Text style={styles.filterAll}>
            <Text style={styles.filter}>Filter:</Text>
            <Text style={styles.all}> All</Text>
          </Text>
        </Text>
      </Text>
      <View style={styles.navigationBar}>
        <View style={styles.segment}>
          <Image
            style={styles.icon1}
            resizeMode="cover"
            source={require("../assets/icon.png")}
          />
          <Text style={[styles.labelText1, styles.mt4]}>Plan</Text>
        </View>
        <View style={styles.segment1}>
          <Image
            style={styles.inactiveicon}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText2, styles.mt8]}>Groceries</Text>
        </View>
        <View style={styles.segment2}>
          <Image
            style={styles.inactiveicon1}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText3, styles.mt8]}>Unnamed</Text>
        </View>
        <View style={styles.segment3}>
          <Image
            style={styles.inactiveicon2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText4, styles.mt8]}>Preferences</Text>
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
        <Text style={styles.labelText5}>See All</Text>
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
  icon: {
    width: "100%",
    height: "100%",
  },
  backButton: {
    position: "absolute",
    left: 16,
    top: 20,
    width: 24,
    height: 24,
  },
  breakfastHeadline: {
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
    bottom: 963,
    left: 0,
    backgroundColor: "#fffbfe",
    width: 360,
  },
  notificationsIcon: {
    position: "absolute",
    top: 76,
    left: 270,
    width: 24,
    height: 24,
  },
  searchTextInput: {
    position: "absolute",
    top: 168,
    left: 16,
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#1c1b1f",
    borderWidth: 1,
    width: 172,
    height: 56,
  },
  labelText: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#1d192b",
    textAlign: "center",
  },
  createButton: {
    position: "absolute",
    top: 176,
    left: 254,
    borderRadius: 100,
    backgroundColor: "#e8def8",
    width: 90,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  lineView: {
    position: "absolute",
    top: 248,
    left: 16,
    borderStyle: "solid",
    borderColor: "#e0dfdf",
    borderTopWidth: 1,
    width: 329,
    height: 1,
  },
  smoothieBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  strawberryBa: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  strawberryBa1: {
    position: "absolute",
    top: 116,
    left: 7,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 172,
    height: 24,
  },
  kJ: {
    position: "absolute",
    top: 139,
    left: 7,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  smoothieImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  smoothieAddButtonCircle: {
    position: "absolute",
    marginTop: -75,
    top: "50%",
    left: 108,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  smoothieAddButtonIcon: {
    position: "absolute",
    height: "8.33%",
    width: "7.82%",
    top: "13.1%",
    right: "24.58%",
    bottom: "78.57%",
    left: "67.6%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  smoothieView: {
    position: "absolute",
    top: 288,
    left: 16,
    width: 179,
    height: 168,
  },
  oatmealBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 169,
  },
  oatmeal: {
    position: "absolute",
    top: 116,
    left: 6,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 20,
  },
  kJ1: {
    position: "absolute",
    top: 139,
    left: 6,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  oatmealImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  oatmealAddButtonCircle: {
    position: "absolute",
    marginTop: -75.5,
    top: "50%",
    left: 107,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  oatmealAddButtonIcon: {
    position: "absolute",
    height: "8.28%",
    width: "8.97%",
    top: "13.02%",
    right: "14.1%",
    bottom: "78.7%",
    left: "76.92%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  oatmealView: {
    position: "absolute",
    top: 288,
    left: 188,
    width: 156,
    height: 169,
  },
  omeletteBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  mushroomOme: {
    position: "absolute",
    top: 115,
    left: 7,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 161,
    height: 24,
  },
  kJ2: {
    position: "absolute",
    top: 139,
    left: 7,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  omeletteImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px2: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  omeletteAddButtonCircle: {
    position: "absolute",
    marginTop: -75,
    top: "50%",
    left: 108,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  omeletteAddButtonIcon: {
    position: "absolute",
    height: "8.33%",
    width: "8.33%",
    top: "13.1%",
    right: "19.64%",
    bottom: "78.57%",
    left: "72.02%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  omeletteView: {
    position: "absolute",
    top: 480,
    left: 16,
    width: 168,
    height: 168,
  },
  soupBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  pumpkinSoup: {
    position: "absolute",
    top: 115,
    left: 7,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  kJ3: {
    position: "absolute",
    top: 139,
    left: 7,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  soupImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px3: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  soupAddButtonCircle: {
    position: "absolute",
    marginTop: -74,
    top: "50%",
    left: 107,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  soupAddButtonIcon: {
    position: "absolute",
    height: "8.33%",
    width: "8.97%",
    top: "13.69%",
    right: "14.1%",
    bottom: "77.98%",
    left: "76.92%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  soupView: {
    position: "absolute",
    top: 672,
    left: 16,
    width: 156,
    height: 168,
  },
  breadBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  sourdoughBread: {
    position: "absolute",
    top: 115,
    left: 7,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  breadImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px4: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  breadAddButtonCircle: {
    position: "absolute",
    marginTop: -74,
    top: "50%",
    left: 106,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  kJ4: {
    position: "absolute",
    top: 139,
    left: 7,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  breadAddButtonIcon: {
    position: "absolute",
    height: "8.33%",
    width: "8.97%",
    top: "13.69%",
    right: "14.74%",
    bottom: "77.98%",
    left: "76.28%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  breadView: {
    position: "absolute",
    top: 672,
    left: 188,
    width: 156,
    height: 168,
  },
  teaBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  earlGreyTea: {
    position: "absolute",
    top: 115,
    left: 7,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  kJ5: {
    position: "absolute",
    top: 139,
    left: 7,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  teaImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px5: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  teaAddButtonCircle: {
    position: "absolute",
    marginTop: -75,
    top: "50%",
    left: 107,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  teaAddButtonIcon: {
    position: "absolute",
    height: "8.33%",
    width: "8.97%",
    top: "13.1%",
    right: "14.1%",
    bottom: "78.57%",
    left: "76.92%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  teaView: {
    position: "absolute",
    top: 864,
    left: 16,
    width: 156,
    height: 168,
  },
  tomatoSaladBorderView: {
    position: "absolute",
    top: 480,
    left: 188,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  tomatoSalad: {
    position: "absolute",
    top: 595,
    left: 195,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  kJ6: {
    position: "absolute",
    top: 619,
    left: 195,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  tomatoSaladImageIcon: {
    position: "absolute",
    top: 481,
    left: 189,
    borderRadius: 9,
    width: 154,
    height: 111,
  },
  iconssettingsFilled24px6: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  tomatoSaladAddButtonCircle: {
    position: "absolute",
    marginTop: -76.5,
    top: "50%",
    left: 295,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  tomatoSaladAddButtonIcon: {
    position: "absolute",
    height: "1.24%",
    width: "3.89%",
    top: "44.39%",
    right: "10.56%",
    bottom: "54.38%",
    left: "85.56%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  tiramisu: {
    position: "absolute",
    top: 115,
    left: 7,
    fontSize: 16,
    letterSpacing: -0.2,
    lineHeight: 24,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    width: 147,
    height: 24,
  },
  tiramisuBoxView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 156,
    height: 168,
  },
  tiramisuImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 154,
    height: 110,
  },
  iconssettingsFilled24px7: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  tiramisuAddButtonBorder: {
    position: "absolute",
    marginTop: -75,
    top: "50%",
    left: 106,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  tiramisuAddButtonIcon: {
    position: "absolute",
    height: "8.33%",
    width: "8.97%",
    top: "13.1%",
    right: "14.74%",
    bottom: "78.57%",
    left: "76.28%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJ7: {
    position: "absolute",
    top: 139,
    left: 7,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 69,
    height: 26,
  },
  tiramisuView: {
    position: "absolute",
    top: 864,
    left: 188,
    width: 156,
    height: 168,
  },
  iconssettingsFilled24px8: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  tuneButtonIcon: {
    position: "absolute",
    marginTop: -389.5,
    top: "50%",
    left: 202,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#1c1b1f",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  tuneButtonIcon1: {
    position: "absolute",
    top: 184,
    left: 210,
    width: 24,
    height: 24,
  },
  filter: {
    color: "#79747e",
  },
  all: {
    color: "#000",
  },
  filterAll: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  filterAllTxtContainer: {
    lineBreak: "anywhere",
    width: "100%",
  },
  filterAll1: {
    position: "absolute",
    top: 254,
    left: 16,
    fontSize: 16,
    letterSpacing: -0.2,
    fontWeight: "600",
    fontFamily: "Open Sans",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 147,
    height: 30,
  },
  icon1: {
    position: "relative",
    width: 64,
    height: 32,
    flexShrink: 0,
  },
  labelText1: {
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
  labelText4: {
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
  labelText5: {
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
  breakfast: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 1131,
    overflow: "hidden",
  },
});

export default Breakfast;
