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

const Foods = () => {
  return (
    <View style={styles.foods}>
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
        <Image
          style={styles.leadingIcon}
          resizeMode="cover"
          source={require("../assets/leadingicon.png")}
        />
        <Text style={styles.headline}>{`Unnamed `}</Text>
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
      <Pressable style={styles.recipesButton}>
        <Text style={styles.labelText}>Recipes</Text>
      </Pressable>
      <Pressable style={styles.foodsButton}>
        <Text style={styles.labelText1}>Foods</Text>
      </Pressable>
      <Pressable style={styles.pantryButton}>
        <Text style={styles.labelText2}>Pantry</Text>
      </Pressable>
      <TextInput
        style={styles.searchTextInput}
        placeholder="Search "
        keyboardType="default"
        placeholderTextColor="#49454f"
      />
      <Pressable style={styles.barcodeScannerCircleButton}>
        <Image
          style={styles.iconssettingsFilled24px}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Pressable style={styles.filterToggleButton}>
        <Image
          style={styles.iconssettingsFilled24px1}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.barcodeScannerIcon}
        resizeMode="cover"
        source={require("../assets/barcode-scanner.png")}
      />
      <View style={styles.lineView} />
      <Text style={styles.filterAll1}>
        <Text style={styles.filterAllTxtContainer}>
          <Text style={styles.filterAll}>
            <Text style={styles.filter}>Filter:</Text>
            <Text style={styles.all}> All</Text>
          </Text>
        </Text>
      </Text>
      <Image
        style={styles.addFoodButtonIcon}
        resizeMode="cover"
        source={require("../assets/add.png")}
      />
      <View style={styles.bananaView}>
        <View style={styles.bananaBorderView} />
        <Text style={styles.banana1}>
          <Text style={styles.banana}>Banana</Text>
        </Text>
        <Pressable style={styles.bananaAddCircleButton}>
          <Image
            style={styles.iconssettingsFilled24px2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.bananaAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
        <Text style={styles.kJPerServing}>{`328 KJ - per serving `}</Text>
        <ImageBackground
          style={styles.bananaImageIcon}
          resizeMode="cover"
          source={require("../assets/bananaimage.png")}
        />
      </View>
      <View style={styles.appleView}>
        <View style={styles.appleBorderView} />
        <Text style={styles.apple1}>
          <Text style={styles.apple}>Apple</Text>
        </Text>
        <Pressable style={styles.appleAddCircleButton}>
          <Image
            style={styles.iconssettingsFilled24px3}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.appleAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
        <Text style={styles.kJPerServing1}>102KJ - per serving</Text>
        <ImageBackground
          style={styles.applesImageIcon}
          resizeMode="cover"
          source={require("../assets/applesimage.png")}
        />
      </View>
      <View style={styles.carrotView}>
        <View style={styles.carrotBorderView} />
        <Text style={styles.carrot1}>
          <Text style={styles.carrot}>Carrot</Text>
        </Text>
        <Pressable style={styles.carrotAddCircleButton}>
          <Image
            style={styles.iconssettingsFilled24px4}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.carrotAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
        <Text style={styles.kJPerServing2}>98 KJ - per serving</Text>
        <ImageBackground
          style={styles.carrotImageIcon}
          resizeMode="cover"
          source={require("../assets/carrotimage.png")}
        />
      </View>
      <View style={styles.cucumberView}>
        <View style={styles.cucumberBorderView} />
        <Text style={styles.cucumber1}>
          <Text style={styles.cucumber}>Cucumber</Text>
        </Text>
        <Pressable style={styles.cucumberAddCircleButton}>
          <Image
            style={styles.iconssettingsFilled24px5}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.cucumberAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
        <Text style={styles.kJPerServing3}>236 KJ - per serving</Text>
        <ImageBackground
          style={styles.cucumbersImageIcon}
          resizeMode="cover"
          source={require("../assets/cucumbersgettyimages6130331805a7c8772a9d4f900367c05a3539118641.png")}
        />
      </View>
      <View style={styles.strawberryView}>
        <View style={styles.strawberryBorder} />
        <Text style={styles.strawberry1}>
          <Text style={styles.strawberry}>Strawberry</Text>
        </Text>
        <Pressable style={styles.strawberryAddCircleButton}>
          <Image
            style={styles.iconssettingsFilled24px6}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.strawberryAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
        <Text style={styles.kJPerServing4}>36 KJ - per serving</Text>
        <ImageBackground
          style={styles.strawberryImageIcon}
          resizeMode="cover"
          source={require("../assets/strawberryimage.png")}
        />
      </View>
      <View style={styles.broccoliView}>
        <View style={styles.broccoliBox} />
        <Text style={styles.broccoli1}>
          <Text style={styles.broccoli}>Broccoli</Text>
        </Text>
        <Pressable style={styles.broccoliAddButtonCircle}>
          <Image
            style={styles.iconssettingsFilled24px7}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
        </Pressable>
        <Image
          style={styles.broccoliAddButtonIcon}
          resizeMode="cover"
          source={require("../assets/bananaaddbutton.png")}
        />
        <Text style={styles.kJPerServing5}>87 KJ - per serving</Text>
        <ImageBackground
          style={styles.broccoliImageIcon}
          resizeMode="cover"
          source={require("../assets/broccoliimage.png")}
        />
      </View>
      <Pressable style={styles.iconButtonToggleable}>
        <Image
          style={styles.iconssettingsFilled24px8}
          resizeMode="cover"
          source={require("../assets/inactiveicon.png")}
        />
      </Pressable>
      <Image
        style={styles.tuneIcon}
        resizeMode="cover"
        source={require("../assets/tune.png")}
      />
      <View style={styles.navigationBar}>
        <View style={styles.segment}>
          <Image
            style={styles.icon}
            resizeMode="cover"
            source={require("../assets/icon.png")}
          />
          <Text style={[styles.labelText3, styles.mt4]}>Plan</Text>
        </View>
        <View style={styles.segment1}>
          <Image
            style={styles.inactiveicon}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText4, styles.mt8]}>Groceries</Text>
        </View>
        <View style={styles.segment2}>
          <Image
            style={styles.inactiveicon1}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText5, styles.mt8]}>Unnamed</Text>
        </View>
        <View style={styles.segment3}>
          <Image
            style={styles.inactiveicon2}
            resizeMode="cover"
            source={require("../assets/inactiveicon.png")}
          />
          <Text style={[styles.labelText6, styles.mt8]}>Preferences</Text>
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
        <Text style={styles.labelText7}>See All</Text>
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
    bottom: 752,
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
  labelText: {
    position: "relative",
    fontSize: 16,
    letterSpacing: 0,
    lineHeight: 20,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  recipesButton: {
    position: "absolute",
    top: 168,
    left: 16,
    borderTopLeftRadius: 100,
    borderBottomLeftRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 109,
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
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  foodsButton: {
    position: "absolute",
    top: 168,
    left: 124,
    backgroundColor: "#e8def8",
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 112,
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
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#49454f",
    textAlign: "center",
  },
  pantryButton: {
    position: "absolute",
    top: 168,
    left: 235,
    borderTopRightRadius: 100,
    borderBottomRightRadius: 100,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 109,
    overflow: "hidden",
    flexDirection: "column",
    paddingHorizontal: 24,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
  },
  searchTextInput: {
    position: "absolute",
    top: 232,
    left: 16,
    borderRadius: 4,
    borderStyle: "solid",
    borderColor: "#1c1b1f",
    borderWidth: 1,
    width: 172,
    height: 56,
  },
  iconssettingsFilled24px: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  barcodeScannerCircleButton: {
    position: "absolute",
    marginTop: -220,
    top: "50%",
    left: 304,
    borderRadius: 100,
    backgroundColor: "#fff",
    borderStyle: "solid",
    borderColor: "#000",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  iconssettingsFilled24px1: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  filterToggleButton: {
    position: "absolute",
    marginTop: -220,
    top: "50%",
    left: 199,
    borderRadius: 100,
    backgroundColor: "#e8def8",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  barcodeScannerIcon: {
    position: "absolute",
    top: 248,
    left: 312,
    width: 24,
    height: 24,
  },
  lineView: {
    position: "absolute",
    top: 312,
    left: 16,
    borderStyle: "solid",
    borderColor: "#e0dfdf",
    borderTopWidth: 1,
    width: 329,
    height: 1,
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
    top: 317,
    left: 17,
    fontSize: 14,
    letterSpacing: -0.2,
    fontWeight: "600",
    fontFamily: "Open Sans",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 147,
    height: 30,
  },
  addFoodButtonIcon: {
    position: "absolute",
    height: "1.52%",
    width: "3.89%",
    top: "27.5%",
    right: "23.06%",
    bottom: "70.98%",
    left: "73.06%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  bananaBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 64,
  },
  banana: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  banana1: {
    position: "absolute",
    top: 6,
    left: 83,
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
  iconssettingsFilled24px2: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  bananaAddCircleButton: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 276,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  bananaAddButtonIcon: {
    position: "absolute",
    height: "21.88%",
    width: "4.27%",
    top: "39.06%",
    right: "7.62%",
    bottom: "39.06%",
    left: "88.11%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJPerServing: {
    position: "absolute",
    top: 30,
    left: 83,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 171,
    height: 26,
  },
  bananaImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 70,
    height: 62,
  },
  bananaView: {
    position: "absolute",
    top: 352,
    left: 16,
    width: 328,
    height: 64,
  },
  appleBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 64,
  },
  apple: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  apple1: {
    position: "absolute",
    top: 6,
    left: 83,
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
  iconssettingsFilled24px3: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  appleAddCircleButton: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 276,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  appleAddButtonIcon: {
    position: "absolute",
    height: "21.88%",
    width: "4.27%",
    top: "39.06%",
    right: "7.62%",
    bottom: "39.06%",
    left: "88.11%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJPerServing1: {
    position: "absolute",
    top: 30,
    left: 83,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 171,
    height: 26,
  },
  applesImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 70,
    height: 62,
  },
  appleView: {
    position: "absolute",
    top: 432,
    left: 16,
    width: 328,
    height: 64,
  },
  carrotBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 64,
  },
  carrot: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  carrot1: {
    position: "absolute",
    top: 6,
    left: 83,
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
  iconssettingsFilled24px4: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  carrotAddCircleButton: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 276,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  carrotAddButtonIcon: {
    position: "absolute",
    height: "21.88%",
    width: "4.27%",
    top: "39.06%",
    right: "7.62%",
    bottom: "39.06%",
    left: "88.11%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJPerServing2: {
    position: "absolute",
    top: 30,
    left: 83,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 171,
    height: 26,
  },
  carrotImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 70,
    height: 62,
  },
  carrotView: {
    position: "absolute",
    top: 512,
    left: 16,
    width: 328,
    height: 64,
  },
  cucumberBorderView: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 64,
  },
  cucumber: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  cucumber1: {
    position: "absolute",
    top: 6,
    left: 83,
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
  iconssettingsFilled24px5: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  cucumberAddCircleButton: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 276,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  cucumberAddButtonIcon: {
    position: "absolute",
    height: "21.88%",
    width: "4.27%",
    top: "39.06%",
    right: "7.62%",
    bottom: "39.06%",
    left: "88.11%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJPerServing3: {
    position: "absolute",
    top: 30,
    left: 83,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 171,
    height: 26,
  },
  cucumbersImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 70,
    height: 62,
  },
  cucumberView: {
    position: "absolute",
    top: 592,
    left: 16,
    width: 328,
    height: 64,
  },
  strawberryBorder: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 64,
  },
  strawberry: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  strawberry1: {
    position: "absolute",
    top: 6,
    left: 83,
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
  iconssettingsFilled24px6: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  strawberryAddCircleButton: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 276,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  strawberryAddButtonIcon: {
    position: "absolute",
    height: "21.88%",
    width: "4.27%",
    top: "39.06%",
    right: "7.62%",
    bottom: "39.06%",
    left: "88.11%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJPerServing4: {
    position: "absolute",
    top: 30,
    left: 83,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 171,
    height: 26,
  },
  strawberryImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 70,
    height: 62,
  },
  strawberryView: {
    position: "absolute",
    top: 672,
    left: 16,
    width: 328,
    height: 64,
  },
  broccoliBox: {
    position: "absolute",
    top: 0,
    left: 0,
    borderRadius: 10,
    borderStyle: "solid",
    borderColor: "#79747e",
    borderWidth: 1,
    width: 328,
    height: 64,
  },
  broccoli: {
    marginBlockStart: 0,
    marginBlockEnd: 0,
  },
  broccoli1: {
    position: "absolute",
    top: 6,
    left: 83,
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
  iconssettingsFilled24px7: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  broccoliAddButtonCircle: {
    position: "absolute",
    marginTop: -20,
    top: "50%",
    left: 276,
    borderRadius: 100,
    backgroundColor: "#8273a9",
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  broccoliAddButtonIcon: {
    position: "absolute",
    height: "21.88%",
    width: "4.27%",
    top: "39.06%",
    right: "7.62%",
    bottom: "39.06%",
    left: "88.11%",
    maxWidth: "100%",
    overflow: "hidden",
    maxHeight: "100%",
  },
  kJPerServing5: {
    position: "absolute",
    top: 30,
    left: 83,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#707070",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 171,
    height: 26,
  },
  broccoliImageIcon: {
    position: "absolute",
    top: 1,
    left: 1,
    borderRadius: 9,
    width: 70,
    height: 62,
  },
  broccoliView: {
    position: "absolute",
    top: 752,
    left: 16,
    width: 328,
    height: 64,
  },
  iconssettingsFilled24px8: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
    overflow: "hidden",
  },
  iconButtonToggleable: {
    position: "absolute",
    marginTop: -220,
    top: "50%",
    left: 250,
    borderRadius: 100,
    borderStyle: "solid",
    borderColor: "#1c1b1f",
    borderWidth: 1,
    flexDirection: "column",
    padding: 8,
    alignItems: "flex-start",
    justifyContent: "flex-start",
  },
  tuneIcon: {
    position: "absolute",
    top: 248,
    left: 207,
    width: 24,
    height: 24,
  },
  icon: {
    position: "relative",
    width: 64,
    height: 32,
    flexShrink: 0,
  },
  labelText3: {
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
  labelText5: {
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
  labelText6: {
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
  labelText7: {
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
  foods: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 920,
    overflow: "hidden",
  },
});

export default Foods;
