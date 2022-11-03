package com.kmu.timetocode

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.kmu.timetocode.R
import android.widget.Toast
import android.content.Intent
import android.view.View
import android.widget.Button
import android.widget.ImageButton
import com.kmu.timetocode.MainActivity

class RecordActivity : AppCompatActivity() {
    var backNotification: ImageButton? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_record)
        backNotification = findViewById<View>(R.id.backNotification) as ImageButton
        backNotification!!.setOnClickListener {
            Toast.makeText(applicationContext, "뒤로가기", Toast.LENGTH_SHORT).show()
            val intent = Intent(applicationContext, MainActivity::class.java)
            startActivity(intent)
        }
    }
}