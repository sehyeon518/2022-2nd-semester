package com.kmu.timetocode

import androidx.appcompat.app.AppCompatActivity
import com.kmu.timetocode.MychallengeActivity.ListViewAdapter
import android.os.Bundle
import com.kmu.timetocode.R
import android.content.Intent
import android.util.Log
import com.kmu.timetocode.MainActivity
import com.kmu.timetocode.ChallengeItem
import android.view.ViewGroup
import android.view.LayoutInflater
import android.view.View
import android.widget.*
import java.util.ArrayList

class MychallengeActivity : AppCompatActivity() {
    var backCertification: ImageButton? = null
    var challengeList: ListView? = null
    var adapter: ListViewAdapter? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_mychallenge)
        backCertification = findViewById<View>(R.id.backCertification) as ImageButton
        backCertification!!.setOnClickListener {
            Toast.makeText(applicationContext, "뒤로가기", Toast.LENGTH_SHORT).show()
            val intent = Intent(applicationContext, MainActivity::class.java)
            startActivity(intent)
        }
        challengeList = findViewById<View>(R.id.challengeList) as ListView
        adapter = ListViewAdapter()
        adapter!!.addItem(
            ChallengeItem(
                "1",
                "챌린지 제목1",
                "1일1커밋을 해보자",
                R.drawable.ic_launcher_background
            )
        )
        adapter!!.addItem(
            ChallengeItem(
                "2",
                "챌린지 제목2",
                "1일1백준을 해보자",
                R.drawable.ic_launcher_background
            )
        )
        adapter!!.addItem(
            ChallengeItem(
                "1",
                "챌린지 제목3",
                "1일1코딩을 해보자",
                R.drawable.ic_launcher_background
            )
        )
        challengeList!!.adapter = adapter
    }

    inner class ListViewAdapter : BaseAdapter() {
        var items = ArrayList<ChallengeItem>()
        override fun getCount(): Int {
            return items.size
        }

        fun addItem(item: ChallengeItem) {
            items.add(item)
        }

        override fun getItem(position: Int): Any {
            return items[position]
        }

        override fun getItemId(position: Int): Long {
            return position.toLong()
        }

        override fun getView(position: Int, convertView: View, viewGroup: ViewGroup): View {
            var convertView = convertView
            val context = viewGroup.context
            val challengeItem = items[position]
            if (convertView == null) {
                val inflater = context.getSystemService(LAYOUT_INFLATER_SERVICE) as LayoutInflater
                convertView = inflater.inflate(R.layout.listview_challenge, viewGroup, false)
            } else {
                var view = View(context)
                view = convertView
            }
            val ch_title = convertView.findViewById<View>(R.id.challengeTitle) as TextView
            val ch_explain = convertView.findViewById<View>(R.id.challengeExplain) as TextView
            val ch_maker = convertView.findViewById<View>(R.id.challengeMaker) as TextView
            //            ImageView ch_icon = (ImageView) convertView.findViewById(R.id.iv_icon);
            ch_title.text = challengeItem.title
            ch_explain.text = challengeItem.num
            //            ch_maker.setImageResource(challengeItem.getResId());
            Log.d("리스트뷰", "getView() - [ " + position + " ] " + challengeItem.title)

            //각 아이템 선택 event
            convertView.setOnClickListener {
                Toast.makeText(
                    context,
                    challengeItem.num + " 번 - " + challengeItem.title + " 입니당! ",
                    Toast.LENGTH_SHORT
                ).show()
            }
            return convertView //뷰 객체 반환
        }
    }
}