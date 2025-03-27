import * as React from "react";
import { useState } from "react";
import { Text, StyleSheet, Image, View, Pressable } from "react-native";
import { useNavigation } from "@react-navigation/native";
import { Checkbox as RNPCheckbox } from "react-native-paper";

const GroceriesAll = () => {
  const navigation = useNavigation();
  const [strawberryCheckboxchecked, setStrawberryCheckboxchecked] =
    useState(undefined);
  const [appleCheckboxchecked, setAppleCheckboxchecked] = useState(undefined);
  const [bananaCheckboxchecked, setBananaCheckboxchecked] = useState(undefined);
  const [carrotCheckboxchecked, setCarrotCheckboxchecked] = useState(undefined);
  const [cucumberCheckboxchecked, setCucumberCheckboxchecked] =
    useState(undefined);
  const [asparagusCheckboxchecked, setAsparagusCheckboxchecked] =
    useState(undefined);
  const [pumpkinCheckboxchecked, setPumpkinCheckboxchecked] =
    useState(undefined);
  const [celeryCheckboxchecked, setCeleryCheckboxchecked] = useState(undefined);
  const [sweetPotatoCheckboxchecked, setSweetPotatoCheckboxchecked] =
    useState(undefined);
  const [mushroomCheckboxchecked, setMushroomCheckboxchecked] =
    useState(undefined);
  const [milkCheckboxchecked, setMilkCheckboxchecked] = useState(undefined);
  const [eggsCheckboxchecked, setEggsCheckboxchecked] = useState(undefined);
  const [cheeseCheckboxchecked, setCheeseCheckboxchecked] = useState(undefined);

  return (
    <View style={styles.groceriesAll}>
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
          style={styles.leadingIcon}
          onPress={() => navigation.goBack()}
        >
          <Image
            style={styles.icon}
            resizeMode="cover"
            source={require("../assets/leadingicon.png")}
          />
        </Pressable>
        <Text style={styles.headline}>Groceries</Text>
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
      <Image
        style={styles.notificationsIcon}
        resizeMode="cover"
        source={require("../assets/notifications1.png")}
      />
      <Pressable style={styles.shopOnlineButton} />
      <Text style={styles.shopOnlineTextButton}>Shop Online</Text>
      <Pressable style={styles.sendListButton} />
      <Text style={styles.sendListTextButton}>Send List</Text>
      <View style={styles.lineView} />
      <Pressable style={styles.allButton}>
        <Text style={styles.labelText}>All</Text>
      </Pressable>
      <Pressable style={styles.byDateButton}>
        <Text style={styles.labelText1}>By Date</Text>
      </Pressable>
      <Pressable style={styles.byRecipeButton}>
        <Text style={styles.labelText2}>By Recipe</Text>
      </Pressable>
      <View style={styles.fruitsView}>
        <View style={styles.strawberryView}>
          <Text style={styles.g}>250 g</Text>
          <Text style={styles.strawberry}>Strawberry</Text>
          <View style={styles.strawberryCheckbox}>
            <RNPCheckbox
              status={strawberryCheckboxchecked ? "checked" : "unchecked"}
              onPress={() =>
                setStrawberryCheckboxchecked(!strawberryCheckboxchecked)
              }
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.appleView}>
          <Text style={styles.text}>3</Text>
          <Text style={styles.apple}>Apple</Text>
          <View style={styles.appleCheckbox}>
            <RNPCheckbox
              status={appleCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setAppleCheckboxchecked(!appleCheckboxchecked)}
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.bananaView}>
          <Text style={styles.text1}>2</Text>
          <Text style={styles.banana}>Banana</Text>
          <View style={styles.bananaCheckbox}>
            <RNPCheckbox
              status={bananaCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setBananaCheckboxchecked(!bananaCheckboxchecked)}
              color="#8273a9"
            />
          </View>
        </View>
        <Text style={styles.fruits}>Fruits</Text>
      </View>
      <View style={styles.vegetablesView}>
        <View style={styles.carrotView}>
          <Text style={styles.carrot}>Carrot</Text>
          <Text style={styles.text2}>3</Text>
          <View style={styles.carrotCheckbox}>
            <RNPCheckbox
              status={carrotCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setCarrotCheckboxchecked(!carrotCheckboxchecked)}
              color="#8273a9"
            />
          </View>
          <View style={styles.cucumberView}>
            <Text style={styles.cucumber}>Cucumber</Text>
            <Text style={styles.text3}>2</Text>
            <View style={styles.cucumberCheckbox}>
              <RNPCheckbox
                status={cucumberCheckboxchecked ? "checked" : "unchecked"}
                onPress={() =>
                  setCucumberCheckboxchecked(!cucumberCheckboxchecked)
                }
                color="#8273a9"
              />
            </View>
          </View>
        </View>
        <View style={styles.asparagusView}>
          <Text style={styles.asparagus}>Asparagus</Text>
          <Text style={styles.g1}>190 g</Text>
          <View style={styles.asparagusCheckbox}>
            <RNPCheckbox
              status={asparagusCheckboxchecked ? "checked" : "unchecked"}
              onPress={() =>
                setAsparagusCheckboxchecked(!asparagusCheckboxchecked)
              }
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.pumpkinView}>
          <Text style={styles.g2}>850 g</Text>
          <Text style={styles.pumpkin}>Pumpkin</Text>
          <View style={styles.pumpkinCheckbox}>
            <RNPCheckbox
              status={pumpkinCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setPumpkinCheckboxchecked(!pumpkinCheckboxchecked)}
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.celeryView}>
          <Text style={styles.text4}>2</Text>
          <Text style={styles.celery}>Celery</Text>
          <View style={styles.celeryCheckbox}>
            <RNPCheckbox
              status={celeryCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setCeleryCheckboxchecked(!celeryCheckboxchecked)}
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.sweetPotatoView}>
          <Text style={styles.g3}>650 g</Text>
          <Text style={styles.sweetPotato}>Sweet Potatoe</Text>
          <View style={styles.sweetPotatoCheckbox}>
            <RNPCheckbox
              status={sweetPotatoCheckboxchecked ? "checked" : "unchecked"}
              onPress={() =>
                setSweetPotatoCheckboxchecked(!sweetPotatoCheckboxchecked)
              }
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.mushroomView}>
          <Text style={styles.g4}>250 g</Text>
          <Text style={styles.mushrooms}>Mushrooms</Text>
          <View style={styles.mushroomCheckbox}>
            <RNPCheckbox
              status={mushroomCheckboxchecked ? "checked" : "unchecked"}
              onPress={() =>
                setMushroomCheckboxchecked(!mushroomCheckboxchecked)
              }
              color="#8273a9"
            />
          </View>
        </View>
        <Text style={styles.vegetables}>Vegetables</Text>
      </View>
      <View style={styles.dairyView}>
        <Text style={styles.dairy}>Dairy</Text>
        <View style={styles.milkView}>
          <Text style={styles.milk}>Milk</Text>
          <Text style={styles.ml}>250 ml</Text>
          <View style={styles.milkCheckbox}>
            <RNPCheckbox
              status={milkCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setMilkCheckboxchecked(!milkCheckboxchecked)}
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.eggsView}>
          <Text style={styles.text5}>3</Text>
          <Text style={styles.eggs}>Eggs</Text>
          <View style={styles.eggsCheckbox}>
            <RNPCheckbox
              status={eggsCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setEggsCheckboxchecked(!eggsCheckboxchecked)}
              color="#8273a9"
            />
          </View>
        </View>
        <View style={styles.cheeseView}>
          <Text style={styles.g5}>150 g</Text>
          <Text style={styles.cheese}>Cheese</Text>
          <View style={styles.cheeseCheckbox}>
            <RNPCheckbox
              status={cheeseCheckboxchecked ? "checked" : "unchecked"}
              onPress={() => setCheeseCheckboxchecked(!cheeseCheckboxchecked)}
              color="#8273a9"
            />
          </View>
        </View>
      </View>
      <View style={styles.navigationBar}>
        <View style={styles.segment}>
          <Image
            style={styles.icon1}
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
      <Image
        style={styles.shoppingCartIcon}
        resizeMode="cover"
        source={require("../assets/groceries.png")}
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
    bottom: 944,
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
  shopOnlineButton: {
    position: "absolute",
    top: 168,
    left: 16,
    borderRadius: 30,
    backgroundColor: "#8273a9",
    width: 156,
    height: 48,
  },
  shopOnlineTextButton: {
    position: "absolute",
    top: 179,
    left: 27,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#fff",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 134,
    height: 26,
  },
  sendListButton: {
    position: "absolute",
    top: 168,
    left: 188,
    borderRadius: 30,
    backgroundColor: "#e8def8",
    width: 156,
    height: 48,
  },
  sendListTextButton: {
    position: "absolute",
    top: 179,
    left: 199,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "center",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: 134,
    height: 26,
  },
  lineView: {
    position: "absolute",
    top: 240,
    left: 16,
    borderStyle: "solid",
    borderColor: "#dbdbdb",
    borderTopWidth: 1,
    width: 329,
    height: 1,
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
  allButton: {
    position: "absolute",
    top: 264,
    left: 16,
    borderTopLeftRadius: 100,
    borderBottomLeftRadius: 100,
    backgroundColor: "#e8def8",
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
  byDateButton: {
    position: "absolute",
    top: 264,
    left: 124,
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
  byRecipeButton: {
    position: "absolute",
    top: 264,
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
  g: {
    position: "absolute",
    top: 4,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  strawberry: {
    position: "absolute",
    top: 2,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  strawberryCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  strawberryView: {
    position: "absolute",
    top: 44,
    left: 0,
    width: 328,
    height: 28,
  },
  text: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  apple: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  appleCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  appleView: {
    position: "absolute",
    top: 85,
    left: 0,
    width: 328,
    height: 28,
  },
  text1: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  banana: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  bananaCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  bananaView: {
    position: "absolute",
    top: 128,
    left: 0,
    width: 328,
    height: 28,
  },
  fruits: {
    position: "absolute",
    top: 0,
    left: 0,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 59,
    height: 26,
  },
  fruitsView: {
    position: "absolute",
    top: 328,
    left: 16,
    width: 328,
    height: 156,
  },
  carrot: {
    position: "absolute",
    top: 2,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  text2: {
    position: "absolute",
    top: 2,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  carrotCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  cucumber: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  text3: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  cucumberCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  cucumberView: {
    position: "absolute",
    top: 129,
    left: 0,
    width: 328,
    height: 28,
  },
  carrotView: {
    position: "absolute",
    top: 44,
    left: 0,
    width: 328,
    height: 157,
  },
  asparagus: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  g1: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  asparagusCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  asparagusView: {
    position: "absolute",
    top: 302,
    left: 0,
    width: 328,
    height: 28,
  },
  g2: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  pumpkin: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  pumpkinCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  pumpkinView: {
    position: "absolute",
    top: 87,
    left: 0,
    width: 328,
    height: 28,
  },
  text4: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  celery: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  celeryCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  celeryView: {
    position: "absolute",
    top: 216,
    left: 0,
    width: 328,
    height: 28,
  },
  g3: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  sweetPotato: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 155,
    height: 22,
  },
  sweetPotatoCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  sweetPotatoView: {
    position: "absolute",
    top: 130,
    left: 0,
    width: 328,
    height: 28,
  },
  g4: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  mushrooms: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  mushroomCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  mushroomView: {
    position: "absolute",
    top: 259,
    left: 0,
    width: 328,
    height: 28,
  },
  vegetables: {
    position: "absolute",
    top: 0,
    left: 0,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 109,
    height: 26,
  },
  vegetablesView: {
    position: "absolute",
    top: 698,
    left: 16,
    width: 328,
    height: 330,
  },
  dairy: {
    position: "absolute",
    top: 0,
    left: 0,
    fontSize: 19,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 59,
    height: 26,
  },
  milk: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  ml: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  milkCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  milkView: {
    position: "absolute",
    top: 44,
    left: 0,
    width: 328,
    height: 28,
  },
  text5: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  eggs: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  eggsCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  eggsView: {
    position: "absolute",
    top: 85,
    left: 0,
    width: 328,
    height: 28,
  },
  g5: {
    position: "absolute",
    top: 3,
    left: 221,
    fontSize: 16,
    lineHeight: 48,
    fontWeight: "600",
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "right",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  cheese: {
    position: "absolute",
    top: 3,
    left: 39,
    fontSize: 16,
    lineHeight: 48,
    fontFamily: "Open Sans",
    color: "#000",
    textAlign: "left",
    display: "flex",
    alignItems: "center",
    width: 107,
    height: 22,
  },
  cheeseCheckbox: {
    position: "absolute",
    top: "50%",
    left: 0,
  },
  cheeseView: {
    position: "absolute",
    top: 128,
    left: 0,
    width: 328,
    height: 28,
  },
  dairyView: {
    position: "absolute",
    top: 512,
    left: 16,
    width: 328,
    height: 156,
  },
  icon1: {
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
    left: 103,
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
  shoppingCartIcon: {
    position: "absolute",
    bottom: 40,
    left: 123,
    width: 24,
    height: 24,
  },
  groceriesAll: {
    position: "relative",
    borderRadius: 20,
    backgroundColor: "#fffbfe",
    flex: 1,
    width: "100%",
    height: 1112,
    overflow: "hidden",
  },
});

export default GroceriesAll;
