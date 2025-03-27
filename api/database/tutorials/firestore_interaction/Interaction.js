import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  TextInput,
} from "react-native";
import { React, useState } from "react";
import {
  AddDataToExistingUser,
  CreateUser,
  RemoveDataToExistingUser,
  RetrieveDocumentID,
  RetrieveDocumentData,
} from "./FSFunctions";

export default function Interaction() {
  const [query, setQuery] = useState("");
  const [userDocId, setUserDocId] = useState("");

  const Heading = () => {
    return (
      <View style={styles.headingContainer}>
        <Text style={{ fontSize: 25, textAlign: "center" }}>
          Interactive FS
        </Text>
        <Text style={{ fontSize: 16 }}>1. id query: enter 2 strings</Text>
        <Text style={{ fontSize: 16 }}>2. add user: enter 4 strings</Text>
        <Text style={{ fontSize: 16 }}>3. data: enter any strings</Text>
      </View>
    );
  };

  const BaseButton = ({ action, text }) => {
    return (
      <View style={styles.buttonContainer}>
        <TouchableOpacity style={styles.touchableButton} onPress={action}>
          <Text style={styles.buttonText}>{text}</Text>
        </TouchableOpacity>
      </View>
    );
  };

  const queryData = () => {
    return query
      .split(/\s+/)
      .map((part) => part.trim())
      .filter((part) => part !== "");
  };

  const Action1 = () => {
    const i = queryData();
    console.log(i);
    // condition for document id query
    if (i.length > 2 || i.length == 0) {
      return;
    }
    RetrieveDocumentID(i[0], i[1]).then((id) => {
      setUserDocId(id.documentId);
      console.log("user id: " + id.documentId);
    });
  };

  const Action2 = () => {
    RetrieveDocumentData(userDocId);
  };

  const Action3 = () => {
    const data = queryData(); //["museums", "opera"];
    AddDataToExistingUser(userDocId, data);
  };

  const Action4 = () => {
    const data = queryData();
    RemoveDataToExistingUser(userDocId, data);
  };

  const Action5 = () => {
    // check if array length
    // is sufficient to create
    // new user
    CreateUser();
  };

  const ClearData = () => {
    setQuery("");
    setUserDocId("");
  };
  return (
    <View style={styles.mainContainer}>
      <Heading />
      <TextInput
        style={styles.inputContainer}
        onChangeText={setQuery}
        value={query}
        placeholder="Enter query or data"
      />
      <BaseButton action={Action1} text="Retrieve id" />
      <BaseButton action={Action2} text="Retrieve data" />
      <BaseButton action={Action3} text="Add to Preferences" />
      <BaseButton action={Action4} text="Remove from Preferences" />
      <BaseButton action={Action5} text="Create user" />
      <BaseButton action={ClearData} text="clear" />
    </View>
  );
}
const styles = StyleSheet.create({
  mainContainer: {
    flex: 1,
    backgroundColor: "#e8e8e8",
    alignItems: "center",
  },
  headingContainer: {
    height: 80,
    verticalAlign: "middle",
  },
  inputContainer: {
    marginVertical: 20,
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
    width: 300,
  },
  buttonContainer: {
    height: 30,
    width: 260,
    margin: 15,
    borderRadius: 15,
    //backgroundColor: "blue",
    alignItems: "center",
    justifyContent: "center",
  },
  touchableButton: {
    position: "absolute",
    height: 30,
    width: 255,
    borderRadius: 15,
    backgroundColor: "#abb8c3",
    alignItems: "center",
  },
  buttonText: {
    fontSize: 17,
    top: "15%",
  },
});
