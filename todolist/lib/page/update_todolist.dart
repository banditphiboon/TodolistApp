import 'package:flutter/material.dart';
// http method package
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

import 'package:todolist/page/todolist.dart';

class UpdatePage extends StatefulWidget {
  final v1, v2, v3;
  const UpdatePage(
    this.v1,
    this.v2,
    this.v3,
  );

  @override
  _UpdatePageState createState() => _UpdatePageState();
}

class _UpdatePageState extends State<UpdatePage> {
  var _v1, _v2, _v3;
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _v1 = widget.v1; //id
    _v2 = widget.v2; //title
    _v3 = widget.v3; //detail
    todo_title.text = _v2;
    todo_detail.text = _v3;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Edit list'),
        actions: [
          IconButton(
              onPressed: () {
                print("Delete ID: $_v1");
                deleteTodo();
                Navigator.pop(context, 'delete'); // เหมือนการกดย้อนกลับ
              },
              icon: Icon(
                Icons.delete,
                color: Colors.black,
              ))
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ListView(
          children: [
            //ช่องกรอกข้อมูล title
            TextField(
                controller: todo_title,
                decoration: InputDecoration(
                    labelText: 'TodoList', border: OutlineInputBorder())),
            SizedBox(
              height: 30,
            ),
            TextField(
                minLines: 3,
                maxLines: 5,
                controller: todo_detail,
                decoration: InputDecoration(
                    labelText: 'detail', border: OutlineInputBorder())),
            SizedBox(
              height: 10,
            ),
            //ปุ่มเพิ่มข้อมูล
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: ElevatedButton(
                onPressed: () {
                  print('------------------------');
                  print('title: ${todo_title.text}');
                  print('detail: ${todo_detail.text}');
                  updateTodo();
                  final snackBar = SnackBar(
                    content: const Text('Update Complete'),
                  );
                  ScaffoldMessenger.of(context).showSnackBar(snackBar);
                },
                child: Text("Edit"),
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all(Colors.amber[900]),
                    padding: MaterialStateProperty.all(
                        EdgeInsets.fromLTRB(50, 20, 50, 20)),
                    textStyle:
                        MaterialStateProperty.all(TextStyle(fontSize: 20))),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future updateTodo() async {
    //var url = Uri.https('bfff-124-120-77-212.ngrok.io', '/api/post-todolist');
    var url = Uri.http('192.168.1.36:8000', '/api/update-todolist/$_v1');
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}","detail":"${todo_detail.text}"}';
    var response = await http.put(url, headers: header, body: jsondata);
    print("---------resut--------");
    print(response.body);
  }

  Future deleteTodo() async {
    var url = Uri.http('192.168.1.36:8000', '/api/delete-todolist/$_v1');
    Map<String, String> header = {"Content-type": "application/json"};
    var response = await http.delete(
      url,
      headers: header,
    );
    print("---------resut--------");
    print(response.body);
  }
}
