//0~100の乱数を発生させて7が出たらwebリクエスト
#include<iostream>
#include<string>
#include<cpprest/http_client.h>

using namespace std;
using namespace web;


void send_webrequest();

int main(){
    int num;
    for(int i = 0; i < 10; i++){
        num = rand()%100;
        cout << num << endl;
        if(num == 7) send_webrequest();
    }
}

void send_webrequest(){
    string event = "random!!";
    string url = "https://maker.ifttt.com/trigger/"+event+"/with/key/d1Ep3s3uUhMZugkBfz5vOQ";

}