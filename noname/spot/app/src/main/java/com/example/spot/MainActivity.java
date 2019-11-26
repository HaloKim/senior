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

        imageView = findViewById(R.id.image);
        addBtn = findViewById(R.id.addBtn);
        layout = findViewById(R.id.line);
        context = this;
        imageView.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent = new Intent();
                intent.setType("image/*");
                intent.setAction(Intent.ACTION_GET_CONTENT);
                startActivityForResult(intent, REQUEST_CODE);
            }
        });

        imageView2 = findViewById(R.id.image2);

        imageView2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent2 = new Intent();
                intent2.setType("image/*");
                intent2.setAction(Intent.ACTION_GET_CONTENT);
                startActivityForResult(intent2, REQUEST_CODE2);
            }
        });
        addBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Button btn = new Button(context);
                btn.setText("버튼" + String.valueOf(count));
                btn.setX(10 + count * 10);
                btn.setY(100 + count * 10);
                btn.setBackgroundColor(Color.argb(0,0,0,0));
                layout.addView(btn);
                count++;
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_CODE ) {
            if (resultCode == RESULT_OK) {
                try {
                    InputStream in = getContentResolver().openInputStream(data.getData());
                    img = BitmapFactory.decodeStream(in);
                    in.close();
                    imageView.setImageBitmap(img);
                    pixels = new int[img.getWidth() * img.getHeight()];
                    img.getPixels(pixels, 0, img.getWidth(), 0, 0, img.getWidth(), img.getHeight());
                    for (int row = 0; row < img.getHeight(); row++)
                        for (int column = 0; column < img.getWidth(); column++)
                            color = Color.valueOf(pixels[row * img.getWidth() + column]);
                } catch (Exception e) {

                }
            } else if (resultCode == RESULT_CANCELED) {
                Toast.makeText(this, "사진 선택 취소", Toast.LENGTH_LONG).show();
            }
        }
        else
        {
            if (resultCode == RESULT_OK) {
                try {
                    InputStream in2 = getContentResolver().openInputStream(data.getData());

                    img2 = BitmapFactory.decodeStream(in2);
                    in2.close();

                    imageView2.setImageBitmap(img2);
                } catch (Exception e) {

                }
            } else if (resultCode == RESULT_CANCELED) {
                Toast.makeText(this, "사진 선택 취소", Toast.LENGTH_LONG).show();
            }
        }

    }
}

    }
}
