import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  final TextEditingController _reviewController = TextEditingController();

  bool _reviewStatus = false;
  String _review = '60% 확률로 부정 리뷰입니다.';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //키보드가 화면 가려 생기는 오류 없애기 위한 설정
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        title: Text('리뷰'),
      ),
      body: Form(
        key: _formKey,
        child: Padding(
          padding: EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextFormField(
                controller: _reviewController,
                decoration: InputDecoration(
                  // hintText: '리뷰',
                  labelText: '리뷰',
                  border: OutlineInputBorder(),
                ),
                validator: (String? value){
                  // if (value == null || value.isEmpty){
                  // 비었거나 null 이면
                  if (value!.isEmpty){
                    return "리뷰를 입력하세요";
                  }
                  return null;
                },
                //  validator가 동작을 수행하는게 아니라 동작하게 만들어줘야함

              ),
              const SizedBox(height: 20.0),
              Container(
                  width: double.infinity,
                  height: 50.0,
                  child: ElevatedButton(
                    onPressed: () async {
                      // state 현재 상태를 나타낼 때
                      // status는 상태가 벌이지고 난 후
                      // 코딩에서는 status 많이 사용
                      // 검증이 되었다면
                      if(_formKey.currentState!.validate()){
                        String review = _reviewController.text;
                        
                        // 각자 환경에 맞게 주소 변경
                        var url = Uri.parse('http://192.168.0.31:5000/inference');
                        var response = await http.post(url, body: {'text': review});
                        if (response.statusCode == 200) {
                          var json = jsonDecode(response.body);
                          double score = json['score'];

                          // 긍정
                          if(score > 0.5) {
                            double result = score * 100;
                            String review = '$result% 확률로 긍정 리뷰 입니다.';
                            setState(() {
                              _review = review;
                              _reviewStatus = true;
                            });
                          }
                          // 부정
                          else {
                            double result = (1-score) * 100;
                            String review = '$result% 확률로 부정 리뷰 입니다.';
                            setState(() {
                              _review = review;
                              _reviewStatus = false;
                            });

                          }
                        }

                        print(review);
                      }
                    },
                    child: const Text(
                      '확인', style: TextStyle(fontSize: 20.0),
                    ),
                  )
              ),
              const SizedBox(height: 50.0),
              Text(
                _review,
                style: TextStyle(
                  fontSize: 25.0,
                  color: _reviewStatus ? Colors.black:Colors.deepOrange,
                ),
              ),
              const SizedBox(height: 20.0),
              Icon(
                _reviewStatus ? Icons.mood : Icons.mood_bad,
                size: 200.0,
                color: _reviewStatus ? Colors.black : Colors.deepOrange,
              ),
            ],
          ),
        )
      )
    );
  }
}