package com.example.spot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.InputStream;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView1 = findViewById(R.id.rightImage);


        ImageView imageView2 = findViewById(R.id.leftImage);



        // 애셋매니저
        AssetManager am = getResources().getAssets();
        InputStream leftImage = null;
        InputStream rightImage = null;

        try {
            // 애셋 폴더에 저장된 0_fake_B.png 열기.
            rightImage = am.open("0_fake_B.png");
            leftImage = am.open("0_real_B.png");


            // 입력스트림 rightImage와 leftImage를 통해 이미지를 Bitmap 객체로 변환.
            Bitmap bm1 = BitmapFactory.decodeStream(rightImage);
            Bitmap bm2 = BitmapFactory.decodeStream(leftImage);


            // 만들어진 Bitmap 객체를 이미지뷰에 표시.
            imageView1.setImageBitmap(bm1);
            imageView2.setImageBitmap(bm2);

            rightImage.close();
            leftImage.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
        if ((rightImage != null )) {
            try {
                rightImage.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

    }
}
