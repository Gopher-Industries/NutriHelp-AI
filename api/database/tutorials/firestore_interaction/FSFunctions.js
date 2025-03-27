import { firebase } from "./config";
import {
  addDoc,
  collection,
  updateDoc,
  arrayUnion,
  arrayRemove,
} from "firebase/firestore";

const db = firebase.firestore();
// methods can be found here:
// https://cloud.google.com/firestore/docs/manage-data/add-data
// tutorial on multiple exports
// https://bobbyhadz.com/blog/react-export-multiple-functions

export async function RetrieveDocumentID(name_first, name_last) {
  var documentId = "";
  try {
    const document = await db
      .collection("User")
      .where("name_first", "==", name_first)
      .where("name_last", "==", name_last)
      //.where("email", "==", "jds@something.com")
      .get();
    if (document.empty) {
      console.log("No matching documents");
    }
    document.forEach((doc) => {
      documentId = doc.id;
      //console.log(doc.id);
    });
  } catch (e) {
    console.log("error retrieving user id", e.message);
  }
  return { documentId };
}

export async function RetrieveDocumentData(user) {
  var documentData = [];
  try {
    const document = await firebase
      .firestore()
      .collection("User")
      .doc(user)
      .get();
    if (!document.exists) {
      alert("no collection");
    } else {
      // replace data1 with the field
      // you wish you retrieve
      // here 'preferences' is used
      documentData = document.data().preferences;
      console.log(documentData);
    }
  } catch (e) {
    console.log("error retrieving user data", e.message);
  }
  return { documentData };
}

export async function AddDataToExistingUser(user, data) {
  try {
    const upload = firebase.firestore().collection("User").doc(user);
    upload.update({
      preferences: arrayUnion(...data),
    });
  } catch (e) {
    console.log("error updating user data ", e.message);
  }
}

export async function RemoveDataToExistingUser(user, data) {
  try {
    const upload = firebase.firestore().collection("User").doc(user);
    upload.update({
      preferences: arrayRemove(...data),
    });
  } catch (e) {
    console.log("error removing user data ", e.message);
  }
}

export async function CreateUser(data) {
  try {
    await addDoc(collection(db, "User"), {
      name_first: "jim",
      name_last: "bob",
      name_middle: "bobby",
      preferences: ["lounging", "karaoke"],
    });
  } catch (e) {
    console.log("error", e.message);
  }
}
