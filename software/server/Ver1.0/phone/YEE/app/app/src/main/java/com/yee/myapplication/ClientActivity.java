package com.yee.myapplication;

import android.content.Intent;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.InetAddress;
import java.net.Socket;

public class ClientActivity extends AppCompatActivity {

    Button btn_send;
    TextView tv_connect,tv_fking;
    EditText ed_sendmsg;
    Handler handler;
    Thread thread,thread2;
    Socket socket = null;
    DataOutputStream out = null;
    DataInputStream in = null;
    InputStream inn;
    String ip;
    String new_s;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_client);
        Intent it = getIntent();
        ip = it.getStringExtra("ip");


        btn_send = (Button)findViewById(R.id.btn_send);
        tv_connect = (TextView)findViewById(R.id.tv_connect);
        tv_fking = (TextView)findViewById(R.id.tv_fking);
        ed_sendmsg = (EditText)findViewById(R.id.ed_sendmsg);
        handler = new Handler();
        thread = new Thread(Connection);
        thread.start();
        thread2 = new Thread(recv);
        thread2.start();
        btn_send.setOnClickListener(Onbtn_sendClick);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        try{
            out.close();
            in.close();
            socket.close();
        }catch (Exception e){

        }
    }

    private Runnable Connection = new Runnable(){
        @Override
        public void run() {
            // TODO Auto-generated method stub
            try{
                InetAddress serverIp = InetAddress.getByName(ip);
                int serverPort = 5000;
                socket = new Socket(serverIp, serverPort);
                tv_connect.setText("connected");
                out = new DataOutputStream(socket.getOutputStream());
                inn = socket.getInputStream();
                in = new DataInputStream(inn);

            }catch(Exception e){
                tv_connect.setText("disconnected");

            }
        }

    };

    private Runnable recv = new Runnable() {
        @Override
        public void run() {
            while(true) {
                try {
                    thread2.sleep(1000);
                    if(socket.isConnected()){
                        int i = inn.available();
                        byte[] a = new byte[i];
                        if(i != 0) {
                            in.read(a);
                            new_s = new String(a);
                        }
                    }
                } catch (Exception e) {

                }

                handler.post(new Runnable() {
                    @Override
                    public void run() {
                        // TODO Auto-generated method stub
                        tv_fking.setText(String.valueOf(new_s));

                    }
                });
            }
        }
    };

    private View.OnClickListener Onbtn_sendClick = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            send();

        }
    };

    void send(){

        if(tv_connect.getText().toString().equals("connected")) {

            new Thread(new Runnable() {    /////////////////////////////////android7.0以上必須將送出放到thread中，否則會閃退
                @Override
                public void run() {
                    try {
                        byte[] b = ed_sendmsg.getText().toString().getBytes();
                        out.write(b);

                    } catch (IOException i) {

                    }

                }
            }).start();

        }
    }
}
