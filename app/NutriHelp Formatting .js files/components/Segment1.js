import * as React from "react";
import {
  StyleProp,
  ViewStyle,
  Image,
  StyleSheet,
  Text,
  View,
} from "react-native";

const Segment1 = ({ style }) => {
  return (
    <View style={[styles.segment, style]}>
      <Image
        style={styles.inactiveicon}
        resizeMode="cover"
        source={require("../assets/inactiveicon.png")}
      />
      <Text style={[styles.labelText, styles.mt8]}>Unnamed</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  mt8: {
    marginTop: 8,
  },
  inactiveicon: {
    position: "relative",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  labelText: {
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
  segment: {
    flex: 1,
    position: "relative",
    height: 80,
    flexDirection: "column",
    paddingHorizontal: 0,
    paddingVertical: 16,
    alignItems: "center",
    justifyContent: "center",
  },
});

export default Segment1;
