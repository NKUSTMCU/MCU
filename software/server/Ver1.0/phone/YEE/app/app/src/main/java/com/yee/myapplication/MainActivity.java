package com.yee.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    Button btn_ok;
    EditText ed_ip;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn_ok = (Button)findViewById(R.id.btn_ok);
        ed_ip = (EditText)findViewById(R.id.ed_ip);
        btn_ok.setOnClickListener(Onbtn_okClick);
    }

    private View.OnClickListener Onbtn_okClick = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            String s = ed_ip.getText().toString();
            if(s.equals(""))
                ed_ip.setText("你的IP?");
            else{
                Intent it = new Intent(MainActivity.this,ClientActivity.class);
                it.putExtra("ip",s);
                startActivity(it);
            }
        }
    };


}
