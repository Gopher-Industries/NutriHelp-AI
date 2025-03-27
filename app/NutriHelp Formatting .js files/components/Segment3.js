import * as React from "react";
import {
  StyleProp,
  ViewStyle,
  Image,
  StyleSheet,
  Text,
  View,
} from "react-native";

const Segment4 = ({ style }) => {
  return (
    <View style={[styles.segment, style]}>
      <Image
        style={styles.icon}
        resizeMode="cover"
        source={require("../assets/icon3.png")}
      />
      <Text style={[styles.labelText, styles.mt4]}>Plan</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  mt4: {
    marginTop: 4,
  },
  icon: {
    position: "relative",
    width: 64,
    height: 32,
    flexShrink: 0,
  },
  labelText: {
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
    position: "relative",
    flexDirection: "column",
    paddingHorizontal: 0,
    paddingTop: 12,
    paddingBottom: 16,
    alignItems: "center",
    justifyContent: "center",
  },
});

export default Segment4;
